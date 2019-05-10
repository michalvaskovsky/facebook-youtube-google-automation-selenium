# -*- coding: utf-8 -*-

from scheduler import Scheduler

class Main(object):

    def __init__(self):
        self.config = 'tmp\\config.txt'
        self.load_ids()

    def load_ids(self):
        with open(self.config, 'r') as f:
            self.ids = f.read().split()

        print ("Ids loaded={}".format(len(self.ids)))
        if len(self.ids) == 0:
            raise Exception("Failed to load profiles from {}".format(self.config))

    def run(self):

        print ("Executing scheduler")
        scheduler = Scheduler(self.ids)
        scheduler.run()

def main():

    m = Main()
    m.run()

main()
