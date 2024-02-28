from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class SearchFilter(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    filter: str = Field(alias="Filter")
    ver: int = Field(alias="Ver")


class Record(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    query: str = Field(alias="Query")
    norm_query: str = Field(alias="NormQuery")
    miner: str = Field(alias="Miner")
    miner_args: str = Field(alias="MinerArgs")
    shard_key: str = Field(alias="ShardKey")
    shard_query: str = Field(alias="ShardQuery")
    preset_args: str = Field(alias="PresetArgs", default="")
    status: str = Field(alias="Status")
    ab_group: str = Field(alias="ABGroup", default="")
    meta_info: str = Field(alias="MetaInfo", default="")
    exp_id: int = Field(alias="ExpID", default=0)
    shard_query2: str = Field(alias="ShardQuery2", default="")
    search_filter: str = Field(alias="SearchFilter", default="")
    default_search_filter: SearchFilter = Field(
        alias="DefaultSearchFilter",
        default=SearchFilter(filter="", ver=0),
    )
    use_shard_query: int = Field(alias="UseShardQuery", default=0)


class ChRecord(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    old: Record = Field(alias="Old")
    new: Record = Field(alias="New")


class CheckInput(BaseModel):
    record: Record
    author: str
    id: int
    force: bool
    perm: int


class CheckOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    record: ChRecord = Field(alias="Record")
    status: int
    passed: bool = Field(alias="Pass")
    logs: str = Field(alias="Logs")


class QueueChanges(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    records: list[Record]
    author: str
    status: int
    timestamp: datetime = Field(alias="timeStamp")
    id: int
    bot: bool
    force: bool


class OutputInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    author: str
    status: int
    status_str: str = Field(alias="statusStr")
    timestamp: datetime = Field(alias="timeStamp")
    id: int
    force: bool
    size: int = Field(alias="Size")


class UserInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str = Field(alias="Name")
    permission: int = Field(alias="Permission")


class IdResponse(BaseModel):
    id: int
