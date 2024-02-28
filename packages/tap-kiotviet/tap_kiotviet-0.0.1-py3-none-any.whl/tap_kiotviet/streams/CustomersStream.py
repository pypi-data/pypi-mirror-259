"""Stream type classes for tap-kiotviet."""

from __future__ import annotations

from  typing import ClassVar, Optional, Dict, Any
from pathlib import Path

from tap_kiotviet.client import KiotVietStream
from tap_kiotviet.kiotviet_paginator import KiotVietPaginator
from .InvoicesStream import InvoicesStream


# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent.parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.

class CustomersStream(KiotVietStream):
    """Define custom stream."""

    name = "customers"
    path = "customers/{customerId}"
    primary_keys: ClassVar[list[str]] = ["id"]
    schema_filepath = SCHEMAS_DIR / "customers.json"  # type: ignore
    replication_method = "FULL_TABLE"  # type: ignore
    records_jsonpath = '*'
    parent_stream_type= InvoicesStream
    
    def get_url_params(
        self, context: Optional[dict], next_page_token: dict
    ) -> Dict[str, Any]:
        params = super().get_url_params(context)

        if next_page_token:
            params.update({"currentItem": int(next_page_token.path)})  # type: ignore

        return params