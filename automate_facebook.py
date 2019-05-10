# -*- coding: utf-8 -*-

import random
import time
import exception_handler
from automate import Automate

class Automate_Facebook(Automate):

    def __init__(self, driver):

        super(Automate_Facebook, self).__init__(driver)

        # facebook related the probability settings
        self.prob_add_friend = (1, 2) # add friends range min, max
        self.range_scroll = (10000, 50000)
        self.range_actions = (10, 30)
        self.range_videos = (1, 3)
        self.range_likes = (1, 3)
        self.delay_actions = (3, 5)
        self.delay_profile = (10, 15)
        self.delay_video_watch = (15, 120)

        self.prob_action_scroll = 10
        self.prob_action_like = 2
        self.prob_action_profile = 1
        self.prob_total = self.prob_action_scroll + self.prob_action_like + self.prob_action_profile

    def friend_send_request(self):
        '''
        Send friend request to a random user. Use the top panel in the personal feed.
        :return: 
        '''

        status = False
        msg = ''
        try:

            self.driver.get('https://www.facebook.com/')

            # open profile
            self.is_visible_by_x('//*[@data-click="profile_icon"]', 60).click()

            # wait for buttons
            self.is_visible_by_x('//*[@aria-label="Add Friend"]', 60)

            # add friend buttons
            # notes: use only first 6 as the rest is not visible and would just raise a exception
            buttons = self.driver.find_elements_by_xpath('//*[@aria-label="Add Friend"]')

            to_add = random.randint(*self.prob_add_friend)
            # pick random button and click
            for button in random.sample(buttons, to_add):
                #button.click()
                self.click_js(button)

                self.sleep_general()

            print ('Sent {} friend requests'.format(to_add))
            status = True

        except Exception as e:
            msg = exception_handler.generic_exception_handler_s(e, exception_handler.func_name())

        return status, msg

    def do_random_like(self):
        '''
        like random post or comment on the current page
        :return: 
        '''

        try:

            elements = self.driver.find_elements_by_xpath('//*/a[contains(text(), "Like")]')
            if len(elements) > 0:

                # click random like
                e = random.sample(elements, 1)[0]
                self.click_js(e)

        except Exception as e:
            pass

    def do_check_profile(self):
        '''
        Open random profile linked at the current page
        :return: 
        '''

        try:

           elements = self.driver.find_elements_by_xpath('//*/a[@class="profileLink"]')
           if len(elements) > 0:
               e = random.sample(elements, 1)[0]
               self.click_js(e)

               # sleep
               time.sleep(random.randint(*self.delay_profile))

               # return to homepage
               self.return_back()

        except Exception as e:
            self.driver.get('https://www.facebook.com/')
            time.sleep(10)

    def news_browse(self):

        status = False
        msg = ''
        try:

            # news feed is on homepage
            self.driver.get('https://www.facebook.com/')

            actions = random.randint(*self.range_actions)
            print ("Number of actions on feeds page={}".format(actions))
            likes = 0
            for i in range(actions):

                # sleep before the action
                time.sleep(random.randint(*self.delay_actions))

                rnd = random.randint(0, self.prob_total)

                # do some actions like scroll
                if 0 <= rnd <= self.prob_action_scroll:
                    self.scroll_down_js(random.randint(*self.range_scroll))
                    print ("Action=Scrolling page...")
                    continue

                rnd -= self.prob_action_scroll
                # add like
                if 0 <= rnd <= self.prob_action_like:
                    print ("Action=Like")
                    self.do_random_like()
                    likes += 1
                    continue

                # check profile
                self.do_check_profile()
                print ("Action=Check profile")

            if likes < 1:
                for i in range(random.randint(*self.range_likes)):
                    self.do_random_like()
                    likes += 1
                    time.sleep(random.randint(*self.delay_actions))

            print ("Likes={}".format(likes))
            status = True

        except Exception as e:
            msg = exception_handler.generic_exception_handler_s(e, exception_handler.func_name())

        return status, msg

    def posts_like(self):

        status = False
        msg = ''
        try:
            pass
        except Exception as e:
            msg = exception_handler.generic_exception_handler_s(e, exception_handler.func_name())

        return status, msg

    def video_watch(self):

        url = 'https://www.facebook.com/watch/latest/'

        status = False
        msg = ''
        try:

            # open page
            self.driver.get(url)

            watch = random.randint(*self.range_videos)
            print ("Watching {} videos".format(watch))
            for i in range(watch):

                # wait for page
                self.is_visible_by_x('//*/button[contains(text(), "Watch")]', 60)

                # get watch buttons
                elements = self.driver.find_elements_by_xpath('//*/button[contains(text(), "Watch")]')

                # click on random
                e = random.sample(elements, 1)[0]
                self.click_js(e)

                # watch for some time
                watch_time = random.randint(*self.delay_video_watch)
                print ("Watching video for {} seconds".format(watch_time))
                time.sleep(watch_time)

                # return to previous page
                self.return_back()

            status = True
        except Exception as e:
            msg = exception_handler.generic_exception_handler_s(e, exception_handler.func_name())

        return status, msg

    def emulate_facebook(self):

        res, msg = self.friend_send_request()
        if not res:
            print ("emulate_facebook.friend_send_request() failed msg=\n\t{}".format(msg))

        res, msg = self.video_watch()
        if not res:
            print ("emulate_facebook.video_watch() failed msg=\n\t{}".format(msg))

        res, msg = self.news_browse()
        if not res:
            print ("emulate_facebook.news_browse() failed msg=\n\t{}".format(msg))

        print ("Emulate facebook finished")



