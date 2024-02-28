"""Stream type classes for tap-kiotviet."""

from __future__ import annotations

from  typing import ClassVar, Optional, Dict, Any
from pathlib import Path

from datetime import date

from tap_kiotviet.client import KiotVietStream
from tap_kiotviet.kiotviet_paginator import KiotVietPaginator


# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent.parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.

class OrdersStream(KiotVietStream):
    """Define custom stream."""

    name = "orders"
    path = "orders"
    primary_keys: ClassVar[list[str]] = ["id",'modifiedDate']
    replication_key = 'modifiedDate'
    schema_filepath = SCHEMAS_DIR / "orders.json"  # type: ignore
    replication_method = "INCREMENTAL"  # type: ignore
    records_jsonpath = 'data[*]'
    
    def get_new_paginator(self):
        """Create a new pagination helper instance.

        If the source API can make use of the `next_page_token_jsonpath`
        attribute, or it contains a `X-Next-Page` header in the response
        then you can remove this method.

        If you need custom pagination that uses page numbers, "next" links, or
        other approaches, please read the guide: https://sdk.meltano.com/en/v0.25.0/guides/pagination-classes.html.

        Returns:
            A pagination helper instance.
        """

        return KiotVietPaginator()
    
    def get_url_params(
        self, context: Optional[dict], next_page_token: dict
    ) -> Dict[str, Any]:
        params = super().get_url_params(context)

        if next_page_token:
            params.update(next_page_token.path)  # type: ignore

        return params