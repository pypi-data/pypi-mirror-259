from unittest import TestCase

from expme import WebshellUtil


class TestWebshellUtil(TestCase):
    def test_check_alive(self):
        util = WebshellUtil(proxy="")
        ok = util.check_alive("GET", "http://localhost:8011/tomcat_test_war_exploded/")
        assert ok
