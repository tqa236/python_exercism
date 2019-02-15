#!/usr/bin/env bash
find . -iname "*.py" | grep -v "test" | xargs pylint
find . -iname "*.py" | grep -v "test" | xargs pydocstyle
