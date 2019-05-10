# -*- coding: utf-8 -*-

from automate_youtube import Automate_Youtube
from selenium import webdriver
import unittest
class test_automate_youtube(unittest.TestCase):

    def test_automate(self):
        d = webdriver.Chrome()
        d.maximize_window()
        a = Automate_Youtube(d)
        a.emulate_youtube()

