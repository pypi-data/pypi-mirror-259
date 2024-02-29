from typing import Dict, List, Any, Optional
from datetime import datetime
from .request import Request

class Shlink:
    _api_key: str = None
    _url: str = None

    def __init__(self, api_key: str, url: str) -> None:
        self._api_key = api_key
        self._url = url.rstrip("/")

    def _get(self, path: str, headers: Dict[str, str] = None):
        return Request.get(url=self._url, api_key=self._api_key, path=path, headers=headers)

    def _post(self, path: str, data: Dict = None, headers: Dict = None):
        return Request.post(url=self._url, api_key=self._api_key, path=path, data=data, headers=headers)

    def list_short_urls(self):
        """
        List all of the short URLs
        :return:
        """
        return self._get("/rest/v3/short-urls")

    def get_short_url(self, short_code: str):
        return self._get(f"/rest/v3/short-urls/{short_code}")
         
    def list_visit_data(self, short_code: str, startDate: Optional[str] = None, excludeBots: bool = True):
        """
        List all of the visit data
        :param short_code: The short code of the URL
        :param startDate: Optional parameter to filter data from a specific start date
        :param excludeBots: Optional parameter to exclude bot visits (default: True)
        :return: Visit data
        """
        params = []
        if startDate is not None:
            params.append(f"startDate={startDate}")
        if excludeBots:
            params.append("excludeBots=true")

        query_string = '&'.join(params)
        if query_string:
            query_string = '?' + query_string

        return self._get(f"/rest/v3/short-urls/{short_code}/visits{query_string}")