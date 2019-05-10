# -*- coding: utf-8 -*-

import io
import json
import time
import random
from automate import Automate
import exception_handler

class Automate_Google(Automate):

    def __init__(self, driver):
        super(Automate_Google, self).__init__(driver)

        self.dictionary_path = 'tmp\\words_dictionary.json'
        self.dictionary = list()

        self.prob_search = (1, 5)
        self.prob_clicks = (1, 3)

    def prepare_vocabulary(self):

        with io.open(self.dictionary_path, 'r') as f:
            js = json.load(f)

        self.dictionary = js.keys()
        print len(self.dictionary)

    def pick_search_term(self):
        try:
            return random.sample(self.dictionary, 1)[0]
        except Exception:
            return ''

    def do_search(self, search_term):

        status = False
        msg = ''
        try:

            # google homepage
            self.driver.get('https://www.google.com/')

            # wait for page to load
            search = self.is_visible_by_x('//*/input[@name="q"]', 60)

            search.send_keys(search_term)
            search.send_keys(u'\ue007')

            # wait for results page
            time.sleep(10)
            self.is_visible_by_x('//*/input[@name="q"]', 60)

            status = True

        except Exception as e:
            msg = exception_handler.generic_exception_handler_s(e, exception_handler.func_name())

        return status, msg

    def click_urls(self, clicks_count):

        status = True
        msg = ''
        try:

            for i in range(clicks_count):
                elems = self.driver.find_elements_by_xpath('//*/a/h3')
                if len(elems) == 0:
                    raise Exception('elems==0')

                e = elems[random.randint(i, len(elems)-1)]
                try:
                    print (u"Clicking={}".format(e.text))
                except Exception:
                    pass
                self.click_js(e)

                # wait
                time.sleep(random.randint(*self.delay_general))

                # return back
                self.return_back()

                # wait
                time.sleep(random.randint(*self.delay_general))

        except Exception as e:
            status = False
            msg = exception_handler.generic_exception_handler_s(e, exception_handler.func_name())

        return status, msg


    def emulate_google(self):

        self.prepare_vocabulary()
        searches = random.randint(*self.prob_search)
        print ("Searches={}".format(searches))

        for i in range(searches):

            search_term = self.pick_search_term()
            if len(search_term) == 0:
                print ("Failed to pick search term.")
                continue

            print ("Running google search for term={}".format(search_term))

            search_res, msg = self.do_search(search_term)
            if not search_res:
                print ("Search failed. message=\n{}".format(msg))
                continue

            clicks = random.randint(*self.prob_clicks)
            click_res, msg = self.click_urls(clicks)
            if not click_res:
                print ("Click failed. message=\n{}".format(msg))

        print ("Finished...")




