# -*- coding: utf-8 -*-
import time
import random

from browser import Browser
from automate_youtube import Automate_Youtube
from automate_google import Automate_Google
from automate_facebook import Automate_Facebook

class Scheduler(object):

    def __init__(self, ids):
        self.ids = ids

        self.big_delay = (9, 13) # delay between sessions min, max in hours

    def sleep_hrs(self, hrs):

        sleep_seconds = hrs * 60 * 60

        for i in range(sleep_seconds):
            time.sleep(1)

    def handle_session(self, ident):

        print ("handling id={}".format(ident))

        browser = Browser()
        driver = browser.initialize_session(ident)
        if driver is None:
            print ("Failed to initialize multilogin session for profile_id={}".format(ident))
            return

        a_youtube = Automate_Youtube(driver)
        a_google = Automate_Google(driver)
        a_facebook = Automate_Facebook(driver)

        a_youtube.emulate_youtube()
        a_google.emulate_google()
        a_facebook.emulate_facebook()

        driver.quit()
        print ("automation finished for id={}".format(ident))

    def handle_sessions(self):

        for i in self.ids:
            self.handle_session(i)

    def run(self):

        while True:

            # do actions
            self.handle_sessions()

            hrs = random.randint(*self.big_delay)
            print ("Next automation session will start in {} hours".format(hrs))
            self.sleep_hrs(hrs)


