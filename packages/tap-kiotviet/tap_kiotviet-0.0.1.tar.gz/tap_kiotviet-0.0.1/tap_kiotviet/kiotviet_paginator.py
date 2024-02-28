"""Stream type classes for tap-kiotviet."""

from __future__ import annotations

import math
from urllib.parse import urlparse, parse_qs

from singer_sdk.pagination import BaseHATEOASPaginator

class KiotVietPaginator(BaseHATEOASPaginator):
    def get_next_url(self, response):
        """
        Return cursor param for next page
        """

        total = response.json().get('total')
        url = urlparse(response.request.url)
        params = parse_qs(url.query, encoding="utf-8")
        currentItem = params.get('currentItem')[0]
        if math.ceil(int(total)/100) > math.floor(int(currentItem)/100)+1:
            return str(int(currentItem)+100)