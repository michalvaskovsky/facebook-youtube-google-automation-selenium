# -*- coding: utf-8 -*-
import time
import random
import exception_handler
from automate import Automate

class Automate_Youtube(Automate):

    def __init__(self, driver):
        super(Automate_Youtube, self).__init__(driver)

        self.prob_videos = (1, 2)
        self.delay_watch = (15, 45)


    def watch_videos(self):

        status = True
        msg = ''
        try:

            self.driver.get('https://youtube.com')

            # wait for page to load
            self.is_visible_by_id("search", 60)

            watches = random.randint(*self.prob_videos)
            print ("Number of videos to check={}".format(watches))

            for i in range(watches):

                # open random video
                elems = self.driver.find_elements_by_xpath('//*/a[@id="thumbnail"]')
                if len(elems)==0:
                    raise Exception("elems==0")

                e = random.sample(elems, 1)[0]
                print ("Opening video href={}".format(e.get_attribute('href')))
                self.click_js(e)

                # watch for some time
                sleep_time = random.randint(*self.delay_watch)
                print ("Sleeping for {} seconds".format(sleep_time))
                time.sleep(sleep_time)

                # return
                self.return_back()

                # wait for page to load
                self.is_visible_by_id("search", 60)

            status = True

        except Exception as e:
            status = False
            msg = exception_handler.generic_exception_handler_s(e, exception_handler.func_name())

        return status, msg

    def emulate_youtube(self):

        res, msg = self.watch_videos()
        if res:
            print ("Finished.")
        else:
            print ("Error. msg=\n{}".format(msg))
