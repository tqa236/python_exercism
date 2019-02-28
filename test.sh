#!/usr/bin/env bash

# find . -iname "*.py" | grep "test" | xargs pytest --cov
pytest --cov=./
