Did I Just Invent That Word?
=============================

Intro
------------------------
I am fond of playing with words and creating/inventing new words. Often I think that I have invented a word, but doing a quick Google-search shows that there are at least 10.000 documents with that word...not too likely that I just invented that word...

This script replies to you (sort of like a magic 8-ball) with random quotes (from a very limited library) in the categories: yes, no, probably yes and probably no, based on the estimated number of documents Google said it found.

Dependencies
------------------------

This script depends on https://code.google.com/p/pygoogle/ for now. It does **NOT** use a Google API key, so if you run the script too many times in quick succession Google will detect that and return nonsense. Fixes for this may or may not be done in near or distant future.

Installation
------------------------

1. # git clone git@github.com:TeeeJay/fun.git
2. # cd fun/did_i_just_invent_that_word
3. # ./setup.sh 
4. # ./src/app.py myword

