from unittest import TestCase

from expme import ServerType, PayloadFormat
from expme import RemotePayloadGenerator, PayloadOptions


class TestRemotePayloadGenerator(TestCase):
    def test_get_payload(self):
        gen = RemotePayloadGenerator()
        opt = PayloadOptions(server=ServerType.TOMCAT, format=PayloadFormat.CLASS_BYTECODE)
        info = gen.get_payload(opt)
        assert len(info.payload) > 0
