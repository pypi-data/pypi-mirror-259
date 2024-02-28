### Пример использования

```Python
import asyncio

from datastoresender.client import DatastoreSender
from datastoresender.model import StorageChanges


async def main():
    async with DatastoreSender("<YOUR_TOKEN>") as client:
        changes: list[StorageChanges] = await client.get_changes()


if __name__ == "__main__":
    asyncio.run(main())
```

или  

```Python
import asyncio

from datastoresender.client import DatastoreSender
from datastoresender.model import StorageChanges


async def main():
    client = DatastoreSender("<YOUR_TOKEN>")

    changes: list[StorageChanges] = await client.get_changes()

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
```

