# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox import options
import exception_handler
import requests

class Browser(object):

    def initialize_session(self, profile_id):
        '''
        :param profile_id: 
        :return: 
        '''

        try:
            mla_url = 'http://127.0.0.1:35000/api/v1/profile/start?automation=true&profileId=' + profile_id
            resp = requests.get(mla_url)

            json = resp.json()

            # Define DesiredCapabilities
            opts = options.DesiredCapabilities()

            # Instantiate the Remote Web Driver to connect to the browser profile launched by previous GET request
            driver = webdriver.Remote(command_executor=json['value'], desired_capabilities={})

            return driver

        except Exception as e:
            exception_handler.generic_exception_handler(e, exception_handler.func_name())
            return None