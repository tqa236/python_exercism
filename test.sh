#!/usr/bin/env bash

# find . -iname "*.py" | grep "test" | xargs pytest --cov
pytest --cov --ignore=minesweeper --ignore=wordy --ignore=ocr-numbers --ignore=poker --ignore=rectangles --ignore=variable-length-quantity --ignore=scale-generator --ignore=connect --ignore=go-counting --ignore=two-bucket --ignore=react --ignore=change --ignore=knapsack --ignore=linked-list  --ignore=bowling --ignore=forth --ignore=grep --ignore=ledger --ignore=pov --ignore=satellite --ignore=transpose --ignore=world-search --ignore=zipper --ignore=queen-attack
