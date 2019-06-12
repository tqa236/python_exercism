#!/usr/bin/env bash

# find . -iname "*.py" | grep "test" | xargs pytest --cov
pytest --cov --ignore=rotational-cipher --ignore=robot-simulator --ignore=atbash-cipher --ignore=say --ignore=secret-handshake --ignore=minesweeper --ignore=wordy --ignore=ocr-numbers --ignore=poker --ignore=rectangles --ignore=binary-search --ignore=variable-length-quantity --ignore=scale-generator --ignore=connect --ignore=go-counting --ignore=two-bucket --ignore=react --ignore=binary-search-tree --ignore=affine-cipher
