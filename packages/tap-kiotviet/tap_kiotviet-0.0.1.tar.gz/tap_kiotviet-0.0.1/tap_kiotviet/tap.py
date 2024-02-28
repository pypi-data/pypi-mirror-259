"""KiotViet tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th
from tap_kiotviet.client import KiotVietStream  # JSON schema typing helpers

# TODO: Import your custom stream types here:
# from tap_kiotviet import kiotviet_paginator

from tap_kiotviet.streams import (
    OrdersStream,
    InvoicesStream,
    CustomersStream,
    BranchesStream,
    ProductsStream,
    UsersStream,
    PurchaseOrdersStream, ReturnsStream
)

STREAM_TYPES = [
    # OrdersStream,
    # InvoicesStream,
    # CustomersStream,
    # BranchesStream,
    # ProductsStream,
    # UsersStream,
    # PurchaseOrdersStream, 
    ReturnsStream
]


class TapKiotViet(Tap):
    """KiotViet tap class."""

    name = "tap-kiotviet"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "client_id",
            th.StringType,
            required=True,
        ),
        th.Property(
            "client_secret",
            th.StringType,
            required=True,
        ),
        th.Property(
            "retailer",
            th.StringType,
            required=True,
        ),
    ).to_dict()

    # TODO: Update this section with the actual config values you expect:

    def discover_streams(self) -> list[KiotVietStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """

        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapKiotViet.cli()
