import base64

from .server import ServerBase, build_session


class WebshellUtil(ServerBase):
    def __init__(self, proxy: str, **kwargs):
        super().__init__(**kwargs)
        self.client = build_session(proxy=proxy)
        self.client_noproxy = build_session()

    def check_alive(self, method: str, url: str):
        uri = self.get_server_url("/config/memshell")
        # get the webshell info must NOT use proxy
        request = self.client_noproxy.get(uri)
        if request.status_code != 200:
            raise Exception(f"Response code is not 200: {request.status_code}, {request.text}")
        info = request.json()
        body = base64.b64decode(info["body"])
        resp = self.client.request(method, url, data=body, headers=info["headers"])
        return info["verify_str"] in resp.text

    def close(self):
        self.client_noproxy.close()
        self.client.close()


if __name__ == "__main__":
    util = WebshellUtil(proxy="http://127.0.0.1:9999")
    ok = util.check_alive("GET", "http://localhost:8011/tomcat_test_war_exploded/")
    print(ok)
