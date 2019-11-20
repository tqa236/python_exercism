#!/usr/bin/env bash

# find . -iname "*.py" | grep "test" | xargs pytest --cov
python3 -m pytest --cov --ignore=minesweeper --ignore=wordy --ignore=poker --ignore=variable-length-quantity --ignore=scale-generator --ignore=connect --ignore=go-counting --ignore=two-bucket --ignore=react --ignore=change --ignore=knapsack --ignore=bowling --ignore=forth --ignore=grep --ignore=ledger --ignore=pov --ignore=satellite --ignore=word-search --ignore=zipper --ignore=book-store --ignore=spiral-matrix --ignore=dominoes --ignore=food-chain --ignore=rest-api
