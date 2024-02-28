"""Stream type classes for tap-kiotviet."""

from __future__ import annotations

from  typing import ClassVar, Iterable, Optional, Dict, Any
from pathlib import Path

from datetime import date
from requests import Response

from tap_kiotviet.client import KiotVietStream
from tap_kiotviet.kiotviet_paginator import KiotVietPaginator


# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent.parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.

class ReturnsStream(KiotVietStream):
    """Define custom stream."""

    name = "returns"
    path = "returns"
    primary_keys: ClassVar[list[str]] = ["id"]
    replication_key = 'modifiedDate'
    schema_filepath = SCHEMAS_DIR / "returns.json"  # type: ignore
    replication_method = "INCREMENTAL"  # type: ignore
    records_jsonpath = '[*]'
    
    def get_new_paginator(self):

        return KiotVietPaginator()
    
    def get_url_params(
        self, context: Optional[dict], next_page_token: dict
    ) -> Dict[str, Any]:
        params = super().get_url_params(context)

        if next_page_token:
            params.update({"currentItem": int(next_page_token.path)})  # type: ignore

        return params

    def parse_response(self, response: Response) -> Iterable[dict]:
        resp_json = response.json()
        data = resp_json.get('data')
        for row in data:
            modifiedDate = row.get('modifiedDate')
            if not modifiedDate:
                row.update({"modifiedDate": row.get("createdDate")})
            yield row