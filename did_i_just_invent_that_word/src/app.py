#!/usr/bin/env python
# -*- coding: utf-8 -*-

from didijustinvent import DidIJustInvent

if __name__ == "__main__":
    import sys
    word = sys.argv[1]

    did_i_just_invent = DidIJustInvent()
    did_i_just_invent.the_word(word)