#!/usr/bin/env bash
# require 'coveralls'
# Coveralls.wear!
find . -iname "*.py" | grep "test" | xargs pytest --cov
