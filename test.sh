#!/usr/bin/env bash

# find . -iname "*.py" | grep "test" | xargs pytest --cov
python3 -m pytest --cov
# python3 -m pytest --cov --ignore=wordy --ignore=variable-length-quantity --ignore=scale-generator --ignore=connect --ignore=go-counting --ignore=two-bucket --ignore=react --ignore=forth --ignore=grep --ignore=ledger --ignore=pov --ignore=satellite --ignore=word-search --ignore=zipper --ignore=pig-latin --ignore=spiral-matrix --ignore=dominoes --ignore=food-chain --ignore=rest-api --ignore=alphametics	--ignore=diffie-hellman --ignore=rail-fence-cipher
