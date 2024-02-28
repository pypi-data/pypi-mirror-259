import unittest

import postlang


class TestModule(unittest.TestCase):
    def failed(self):
        self.failed = True

    def setUp(self):
        self.failed = False
        postlang.api_key = "testsecret"
        postlang.host = "http://localhost:8000"
        postlang.on_error = self.failed

    def test_no_api_key(self):
        postlang.api_key = None
        self.assertRaises(Exception, postlang.capture)

    def test_no_host(self):
        postlang.host = None
        self.assertRaises(Exception, postlang.capture)

    def test_track(self):
        postlang.capture("distinct_id", "python module event")
        postlang.flush()

    def test_identify(self):
        postlang.identify("distinct_id", {"email": "user@email.com"})
        postlang.flush()

    def test_alias(self):
        postlang.alias("previousId", "distinct_id")
        postlang.flush()

    def test_page(self):
        postlang.page("distinct_id", "https://github.com/postlang")
        postlang.flush()

    def test_flush(self):
        postlang.flush()
