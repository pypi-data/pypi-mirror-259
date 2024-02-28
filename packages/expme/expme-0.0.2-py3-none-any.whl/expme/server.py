import functools
import logging
import os
from typing import Dict

import urllib3
from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

urllib3.disable_warnings()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.util.ssl_.DEFAULT_CIPHERS = "ALL"

logger = logging.getLogger(__file__)

request_default_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Cache-Control": "max-age=0",
    "DNT": "1",
    "Upgrade-Insecure-Requests": "1",
}


class ServerBase:
    def __init__(self, *args, **kwargs):
        self.API_VERSION = "v1"
        self.BASE_URL = "http://127.0.0.1:8090"

        if os.getenv("EXPLOIT_BASE_URL"):
            self.BASE_URL = os.getenv("EXPLOIT_BASE_URL")
        if self.BASE_URL.endswith("/"):
            self.BASE_URL = self.BASE_URL[:-1]

    def get_server_url(self, path):
        if path.startswith("/"):
            path = path[1:]
        return f"{self.BASE_URL}/{self.API_VERSION}/{path}"


# Don't forget to close session
def build_session(headers: Dict[str, str] = None, timeout=10, proxy: str = None, **kwargs):
    session = Session()

    # patch default timeout
    session.request = functools.partial(session.request, timeout=timeout)

    session.trust_env = False
    if proxy:
        session.proxies = {
            "http": proxy,
            "https": proxy,
        }

    # ignore ssl
    session.verify = False

    # setup default headers
    header = request_default_headers.copy()
    if headers:
        header.update(headers)
    session.headers.update(header)

    # retry policy
    retries = Retry(
        total=2,
        redirect=3,
        backoff_factor=1,
        status_forcelist=[502, 503, 504],
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))
    session.mount("http://", HTTPAdapter(max_retries=retries))

    return session
