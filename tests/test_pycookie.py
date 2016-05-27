from unittest import TestCase

import pycookie

class TestCookie(TestCase):

    def test_is_string(self):
        s = pycookie.cutter()
        self.assertTrue(isinstance(s, basestring))


    def test_basic(self):
        from pycookie.command_line import main
        main()
