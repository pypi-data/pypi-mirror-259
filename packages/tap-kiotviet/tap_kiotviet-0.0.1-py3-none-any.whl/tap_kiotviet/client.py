"""REST client handling, including KiotVietStream base class."""

from __future__ import annotations
from datetime import date

from pathlib import Path
from typing import Any, Callable, Iterable

import requests

from singer_sdk.authenticators import OAuthAuthenticator, BearerTokenAuthenticator
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.pagination import BaseAPIPaginator  # noqa: TCH002
from singer_sdk.streams import RESTStream

_Auth = Callable[[requests.PreparedRequest], requests.PreparedRequest]
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class KiotVietOauth(OAuthAuthenticator):

    auth_endpoint = "https://id.kiotviet.vn/connect/token"

    @property
    def client_id(self) -> str:
        """
        Get client ID string to be used in authentication.

        RETURNS:
        Optional client secret from stream config if it has been set."""
        return self.config.get("client_id")

    @property
    def client_secret(self) -> str:
        """Get client secret to be used in authentication.

        RETURNS:
        Optional client secret from stream config if it has been set."""
        return self.config.get("client_secret")

    @property
    def oauth_request_body(self) -> dict:
        """RAISES:
        NotImplementedError – If derived class does not override this method."""
        return {
            "scope": self.oauth_scopes,
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

    @property
    def oauth_scopes(self) -> str:
        return "PublicApi.Access"


class KiotVietStream(RESTStream):
    """KiotViet stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        # TODO: hardcode a value here, or retrieve it from self.config
        return "https://public.kiotapi.com/"

    records_jsonpath = "$[*]"  # Or override `parse_response`.

    # Set this value or override `get_new_paginator`.
    # next_page_token_jsonpath = "$.next_page"  # noqa: S105

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Return a new authenticator object.

        Returns:
            An authenticator instance.
        """
        client = KiotVietOauth(stream=self)
        client.update_access_token()
        access_token = client.access_token
        return BearerTokenAuthenticator.create_for_stream(self, token=access_token)

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")

        headers["Retailer"] = self.config.get("retailer")
        # If not using an authenticator, you may also provide inline auth headers:
        # headers["Private-Token"] = self.config.get("auth_token")  # noqa: ERA001
        return headers

    def get_new_paginator(self) -> BaseAPIPaginator:
        """Create a new pagination helper instance.

        If the source API can make use of the `next_page_token_jsonpath`
        attribute, or it contains a `X-Next-Page` header in the response
        then you can remove this method.

        If you need custom pagination that uses page numbers, "next" links, or
        other approaches, please read the guide: https://sdk.meltano.com/en/v0.25.0/guides/pagination-classes.html.

        Returns:
            A pagination helper instance.
        """
        return super().get_new_paginator()

    def get_url_params(
        self,
        context: dict | None,  # noqa: ARG002
        # next_page_token: Any | None,  # noqa: ANN401
        *args,
    ) -> dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """

        params: dict = {}
        params["currentItem"] = 0
        # if next_page_token:
        #     params.update(parse_qsl(next_page_token.query))
        if self.replication_key:
            params["orderDirection"] = "asc"
            params["sort"] = self.replication_key
        params["pageSize"] = 100
        params['lastModifiedFrom']= self.config.get('start_date')
        params['toDate'] = date.today().isoformat()

        return params

    def prepare_request_payload(
        self,
        context: dict | None,  # noqa: ARG002
        next_page_token: Any | None,  # noqa: ARG002, ANN401
    ) -> dict | None:
        """Prepare the data payload for the REST API request.

        By default, no payload will be sent (return None).

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary with the JSON body for a POST requests.
        """
        # TODO: Delete this method if no payload is required. (Most REST APIs.)
        return None

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records.

        Args:
            response: The HTTP ``requests.Response`` object.

        Yields:
            Each record from the source.
        """
        # TODO: Parse response body and return a set of records.
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    def post_process(
        self,
        row: dict,
        context: dict | None = None,  # noqa: ARG002
    ) -> dict | None:
        """As needed, append or transform raw data to match expected structure.

        Args:
            row: An individual record from the stream.
            context: The stream context.

        Returns:
            The updated record dictionary, or ``None`` to skip the record.
        """
        # TODO: Delete this method if not needed.
        return row
