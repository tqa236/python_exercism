#!/usr/bin/env bash
# find . -iname "*.py" | grep -v "test" | xargs pylint
# find . -iname "*.py" | grep -v "test" | xargs pylint | grep "10.00/10" | wc -l
find . -iname "*.py" | grep -v "test" | xargs pydocstyle
