import aiohttp
import asyncio
import json
import logging
from http import HTTPMethod

from .exceptions import NotAllowedError
from .iterutils import batched
from .model import (
    UserInfo,
    Record,
    CheckInput,
    CheckOutput,
    OutputInfo,
    QueueChanges,
    IdResponse,
)


class DatastoreSender:
    BASE_URLS = [
        "http://datastore-proxy.wbx-search.svc.k8s.wbxsearch-el",
        "http://datastore-proxy.wbx-search.svc.k8s.wbxsearch-dl",
    ]
    BATCH_SIZE = 1000
    TIMEOUT = 3
    RETRIES = 3
    RETRY_INTERVAL = 0.2

    def __init__(self, token: str, debug: bool = False) -> None:
        self.__user: UserInfo | None = None
        self.token: str = token
        self.debug: bool = debug

        self.session = aiohttp.ClientSession(
            raise_for_status=True,
            timeout=aiohttp.ClientTimeout(total=self.TIMEOUT),
            headers={
                "Content-Type":  "application/json;charset=utf-8",
                "Authorization": f"Bearer {token}",
            },
        )

    async def __aenter__(self) -> "DatastoreSender":
        return self

    async def __aexit__(self, *args):
        await self.close()

    async def close(self):
        return await self.session.close()

    async def send_records(self, records: list[Record]) -> int:
        return await self.__send_records(records, False)

    async def send_records_force(self, records: list[Record]) -> int:
        await self.__ensure_auth()

        if self.__user.permission < 1:
            raise NotAllowedError()

        return self.__send_records(records, True)

    async def get_changes(self) -> list[OutputInfo]:
        """
        Получение информации об отправках по токену пользователя
        """

        urls = self.__make_urls("api/v1/getChanges")

        data = await self.__request(HTTPMethod.GET, urls)

        return [OutputInfo(**d) for d in data]

    async def get_changes_by_author(self) -> list[OutputInfo]:
        """
        Получение информации об отправках по токену пользователя и автору
        onlyFailed: только зафейленные отправки
        """

        await self.__ensure_auth()

        urls = self.__make_urls("api/v1/getChangesByAuthor")

        data = await self.__request(HTTPMethod.GET, urls, params={
            "author": self.__user.name,
        })

        return [OutputInfo(**d) for d in data]

    async def get_change_by_id(self, id: int, only_failed: bool) -> list[CheckOutput]:
        """
        Получение информации об отправках по токену пользователя и id изенения
        onlyFailed: только зафейленные отправки
        """

        urls = self.__make_urls("api/v1/getChangeFromStorageId")

        data = await self.__request(HTTPMethod.GET, urls, params={
            "id": id,
            "onlyFailed": "true" if only_failed else "false",
        })

        return [CheckOutput(**d) for d in data]

    async def get_record_by_id_from_queue(self, id: int) -> QueueChanges:
        """
        Получение записи из очередчи по токену пользователя и id изменения
        """

        urls = self.__make_urls("api/v1/getRecordFromQueueId")

        data = await self.__request(HTTPMethod.GET, urls, params={
            "id": id,
        })

        return QueueChanges(**data)

    async def get_change_status(self, id: int) -> int:
        """
        Получение статуса изменения по id
        """

        urls = self.__make_urls("api/v1/getRecordStatus")

        data = await self.__request(HTTPMethod.GET, urls, params={
            "id": id,
        })

        status = int(data)

        return status

    async def get_basket(self) -> list[Record]:
        await self.__ensure_auth()

        urls = self.__make_urls("api/v1/getBasketByAuthor")

        data = await self.__request(HTTPMethod.GET, urls, params={
            "author": self.__user.name,
        })

        return [Record(**d) for d in data]
    
    async def add_to_basket(self, records: list[Record]) -> None:
        await self.__add_to_basket(records, False)
    
    async def add_to_basket_force(self, records: list[Record]) -> None:
        await self.__ensure_auth()

        if self.__user.permission < 1:
            raise NotAllowedError()
        
        await self.__add_to_basket(records, True)
    
    async def __add_to_basket(self, records: list[Record], force: bool) -> None:
        await self.__ensure_auth()
        id: int = await self.__get_id()

        input: list[CheckInput] = []

        for record in records:
            check = CheckInput(
                perm=self.__user.permission,
                author=self.__user.name,
                record=record,
                id=id,
                force=force,
            )

            input.append(check)

        await self.__send_to_basket(input)
    
    async def __send_to_basket(self, checks: list[CheckInput]) -> None:
        urls = self.__make_urls("api/v1/addBatchToBasket")

        payload = [check.model_dump(by_alias=True) for check in checks]

        await self.__request("POST", urls, json=payload)
    
    async def push_basket(self) -> None:
        await self.__ensure_auth()

        urls = self.__make_urls("api/v1/addToQueue")

        await self.__request(HTTPMethod.POST, urls, params={
            "author": self.__user.name,
        })

    async def __send_records(self, records: list[Record], force: bool) -> int:
        """
        Отправляет данные на прокси с токеном
        """

        await self.__ensure_auth()
        id = await self.__get_id()

        batches = batched(records, self.BATCH_SIZE)
        tasks = []

        for batch in batches:
            checks: list[CheckInput] = []

            for record in batch:
                check = CheckInput(
                    record=record,
                    author=self.__user.name,
                    id=id,
                    force=force,
                    perm=0,
                )

                checks.append(check)

            tasks.append(self.__push_checker(checks))

        exceptions = await asyncio.gather(*tasks, return_exceptions=True)

        for exception in exceptions:
            if exception is not None:
                logging.error(f"[DATASENDER][SEND_REC][ERROR]: {exception}")

        return id

    async def __get_id(self) -> int:
        """
        Получить id из чекера
        """

        urls = self.__make_urls("api/v1/getId")

        data = await self.__request(HTTPMethod.GET, urls)

        return IdResponse(**data).id

    async def __push_checker(self, checks: list[CheckInput]) -> None:
        urls = self.__make_urls("api/v1/push-checker")

        payload = [check.model_dump(by_alias=True) for check in checks]

        await self.__request("POST", urls, json=payload)

    async def __auth(self) -> UserInfo:
        urls = self.__make_urls("auth")

        data = await self.__request(HTTPMethod.GET, urls)

        return UserInfo(**data)

    async def __ensure_auth(self) -> None:
        if self.__user is None:
            self.__user = await self.__auth()

    def __make_urls(self, path: str) -> list[str]:
        base_urls = self.BASE_URLS

        if self.debug:
            base_urls = [
                base_url.replace("datastore-proxy", "datastore-proxy-test", 1)
                for base_url in base_urls
            ]

        return [f"{base_url}/{path}" for base_url in base_urls]

    async def __request(self, method: HTTPMethod, urls: list[str], **kwargs):
        result = None
        exception = None

        for _ in range(self.RETRIES):
            for url in urls:
                try:
                    async with self.session.request(method, url, **kwargs) as resp:
                        resp_text = await resp.text()
                        result = json.loads(resp_text)

                    break
                except json.decoder.JSONDecodeError as exc:
                    # прилетела не json строка
                    # если это пустая строка, то все ок
                    # и клиент не должен ожидать никакой ответ как, например, в __push_checker
                    if resp_text == "":
                        # костыль
                        # присвоим пустой дикт, чтобы выйти из цикла retries
                        result = {}
                        break

                    # TODO: нормально обрабатывать такие моменты
                    # если какая-то другая строка, например, "not found",
                    # то запрос был сделан неправильно клиентом
                    raise Exception(f"request failed: {resp_text}")
                except aiohttp.ClientError as exc:
                    logging.error(exc)
                    exception = exc
                    continue

            if result is None:
                await asyncio.sleep(self.RETRY_INTERVAL)
                continue

            break

        if result is None and exception is not None:
            raise exception

        return result
