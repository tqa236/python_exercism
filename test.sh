#!/usr/bin/env bash

# find . -iname "*.py" | grep "test" | xargs pytest --cov
pytest --cov --ignore=minesweeper --ignore=wordy --ignore=ocr-numbers --ignore=poker --ignore=rectangles --ignore=variable-length-quantity --ignore=scale-generator --ignore=connect --ignore=go-counting --ignore=two-bucket --ignore=react --ignore=binary-search-tree --ignore=affine-cipher --ignore=change --ignore=crypto-square --ignore=dot-dsl --ignore=house --ignore=knapsack --ignore=linked-list --ignore=list-ops --ignore=queen-attack --ignore=simple-linked-list
