#!/usr/bin/env bash

# find . -iname "*.py" | grep "test" | xargs pytest --cov
# python3 -m pytest --cov
python3 -m pytest --cov --ignore=scale-generator --ignore=connect --ignore=go-counting --ignore=two-bucket --ignore=grep --ignore=pov --ignore=zipper --ignore=dominoes --ignore=rail-fence-cipher --ignore=forth --ignore=pascals-triangle
