# -*- coding: utf-8 -*-

import sys
import random
import time

from extlibs.pygoogle import pygoogle as google


__author__ = 'teeejay'
__version__ = 0.1


class DidIJustInvent:

    yes = ['Yep!', 'Wooha!']
    no = ['Nop!', 'Really?']
    maybe_yes = ['Maybe', 'May seem so', 'Not unlikely', 'Don\'t count on it']
    maybe_no = ['Probably not', 'Unlikely', 'I wouldn\'t bet on it']

    ranges = [('no', 50), ('maybe_no',10), ('maybe_yes', 1), ('yes', 0)]

    def __init__(self):
        self.word = ''

    def the_word(self, word):
        result = google.pygoogle(word)
        result_count = result.get_result_count()

        ans = max([range for range in self.ranges if int(result_count) >= range[1]],key=lambda x:x[1])
        var = getattr(self,ans[0])

        random.seed(time.time())
        rand = random.randint(0,len(var)-1)
        print str(var[rand])

        print "(approx # documents with that word: %s)" % str(result_count)
