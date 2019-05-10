# -*- coding: utf-8 -*-
import random
import time
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Automate(object):

    def __init__(self, driver):
        self.driver = driver

        # delay
        self.delay_general = (3, 7)

    def is_visible_by_x(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))

    def is_visible_by_no_raise_by_x(self, locator, timeout=10):
        try:
            return self.is_visible_by_x(locator, timeout)
        except Exception:
            return None

    def is_visible_by_id(self, id, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.ID, id)))

    def is_visible_by_name(self, name, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.NAME, name)))

    def is_checked_by_name(self, name):
        return self.driver.find_element_by_name(name).is_selected()

    def click_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def click_javascript_by_x(self, locator):
        '''
        Click by executing a javascript when normal element.click() doesn't work
        :param locator: element locator 
        :return: None
        '''
        elem = self.driver.find_element_by_xpath(locator)
        self.driver.execute_script("arguments[0].click();", elem)

    def scroll_to_bottom_js(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_down_js(self, height):
        self.driver.execute_script("window.scrollTo(0, {});".format(height))

    def scroll_down_js_slow(self, height, step=500):

        for i in range(0, height, step):
            self.scroll_down_js(step)
            time.sleep(1)

    def sleep_general(self):
        time.sleep(random.randint(*self.delay_general))

    def return_back(self):
        '''
        Return to previous page        
        :return: 
        '''
        self.driver.execute_script("window.history.go(-1)")


