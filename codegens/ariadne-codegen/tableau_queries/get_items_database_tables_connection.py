# Generated by ariadne-codegen
# Source: ./tableau-queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import RemoteType


class GetItemsDatabaseTablesConnection(BaseModel):
    database_tables_connection: (
        "GetItemsDatabaseTablesConnectionDatabaseTablesConnection"
    ) = Field(alias="databaseTablesConnection")


class GetItemsDatabaseTablesConnectionDatabaseTablesConnection(BaseModel):
    nodes: List["GetItemsDatabaseTablesConnectionDatabaseTablesConnectionNodes"]
    page_info: "GetItemsDatabaseTablesConnectionDatabaseTablesConnectionPageInfo" = (
        Field(alias="pageInfo")
    )


class GetItemsDatabaseTablesConnectionDatabaseTablesConnectionNodes(BaseModel):
    id: str
    is_embedded: Optional[bool] = Field(alias="isEmbedded")
    columns: List[
        "GetItemsDatabaseTablesConnectionDatabaseTablesConnectionNodesColumns"
    ]


class GetItemsDatabaseTablesConnectionDatabaseTablesConnectionNodesColumns(BaseModel):
    remote_type: RemoteType = Field(alias="remoteType")
    name: Optional[str]


class GetItemsDatabaseTablesConnectionDatabaseTablesConnectionPageInfo(BaseModel):
    has_next_page: bool = Field(alias="hasNextPage")
    end_cursor: Optional[str] = Field(alias="endCursor")


GetItemsDatabaseTablesConnection.model_rebuild()
GetItemsDatabaseTablesConnectionDatabaseTablesConnection.model_rebuild()
GetItemsDatabaseTablesConnectionDatabaseTablesConnectionNodes.model_rebuild()
