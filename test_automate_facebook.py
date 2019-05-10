# -*- coding utf-8 -*-

from automate_facebook import Automate_Facebook
import exception_handler
import unittest

class test_automate_facebook(unittest.TestCase):

    def test_1(self):
        a = Automate_Facebook('test')
        assert (a)
