#!/usr/bin/env bash

mkdir -p src/extlibs/pygoogle && svn checkout http://pygoogle.googlecode.com/svn/trunk/ src/extlibs/pygoogle
touch src/extlibs/__init__.py
touch src/extlibs/pygoogle/__init__.py
