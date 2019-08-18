#!/usr/bin/env bash

# find . -iname "*.py" | grep "test" | xargs pytest --cov
pytest --cov --ignore=minesweeper --ignore=wordy --ignore=ocr-numbers --ignore=poker --ignore=rectangles --ignore=variable-length-quantity --ignore=scale-generator --ignore=connect --ignore=go-counting --ignore=two-bucket --ignore=react --ignore=binary-search-tree --ignore=change --ignore=knapsack --ignore=linked-list --ignore=queen-attack
