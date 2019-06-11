#!/usr/bin/env bash
# Automatically test all exercises
for path in */; do
    [ -d "${path}" ] || continue # if not a directory, skip
    dirname="$(basename "${path}")"
    cd "$dirname" || exit
    file_name=${path::-1}
    file_name=${file_name//-/_}
    # echo "$file_name"
    monkeytype run "${file_name}_test.py"
    monkeytype apply "${file_name}"
    cd .. || exit
done
