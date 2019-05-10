# -*- coding: utf-8 -*-

from automate_facebook import Automate_Facebook
from automate_google import Automate_Google
from browser import Browser
import time

class Test_Tasks(object):

    def __init__(self):
        self.profile_id_test = 'PROFILE_ID'

    def load_browser(self):
        browser = Browser()
        self.driver = browser.initialize_session(self.profile_id_test)
        if self.driver is None:
            raise Exception("Failed to initialize driver")

    # add friends test
    def test_facebook_1(self):
        auto = Automate_Facebook(self.driver)
        return auto.friend_send_request()

    def test_facebook_2(self):
        auto = Automate_Facebook(self.driver)
        return auto.news_browse()

    def test_facebook_3(self):
        auto = Automate_Facebook(self.driver)
        return auto.video_watch()

    def test_facebook_4(self):
        auto = Automate_Facebook(self.driver)
        return auto.emulate_facebook()

    def test_google(self):
        auto = Automate_Google(self.driver)
        return auto.emulate_google()

def run():

    t = Test_Tasks()
    t.load_browser()

    # add facebook friend
    res, message = t.test_facebook_4()
    #res, message = t.test_google()
    print res, message
    t.driver.quit()
    time.sleep(1000)

run()



