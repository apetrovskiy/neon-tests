import requests
import typing as tp
import urllib.parse
from busypie import wait_at_most, MINUTE
from http import HTTPStatus


class Faucet:
    def __init__(self, faucet_url: str, session: tp.Optional[tp.Any] = None):
        self._url = faucet_url
        self._session = session or requests.Session()

    def request_neon(self, address: str, amount: int = 100):
        assert address.startswith("0x")
        url = urllib.parse.urljoin(self._url, "request_neon")
        # resp = self._session.post(url, json={"amount": amount, "wallet": address})
        wait_at_most(MINUTE).until(lambda: HTTPStatus.OK == self.send_post_request(url, address, amount).status_code)
        # assert resp.status_code == 200, resp.text

    def send_post_request(self, url: str, address: str, amount: int):
        return self._session.post(url, json={"amount": amount, "wallet": address})
