# -*- coding: utf-8 -*-
import unittest
from automate_google import Automate_Google
from selenium import webdriver

class test_automate_google(unittest.TestCase):

    def test_init(self):
        a = Automate_Google(None)
        a.prepare_vocabulary()
        assert True

    def test_operate(self):
        driver = webdriver.Chrome()
        driver.maximize_window()

        a = Automate_Google(driver)
        a.prepare_vocabulary()
        a.emulate_google()

