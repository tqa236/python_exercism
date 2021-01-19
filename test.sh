#!/usr/bin/env bash

# find . -iname "*.py" | grep "test" | xargs pytest --cov
# python3 -m pytest --cov
python3 -m pytest --cov --ignore=wordy --ignore=scale-generator --ignore=connect --ignore=go-counting --ignore=two-bucket --ignore=grep --ignore=ledger --ignore=pov --ignore=word-search --ignore=zipper --ignore=pig-latin --ignore=spiral-matrix --ignore=dominoes --ignore=rail-fence-cipher
