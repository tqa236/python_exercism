#!/bin/bash

# Get a list of Python files changed in git diff
changed_files=$(git diff --name-only -- '*.py' | grep -v 'test')

# Check if there are any Python files changed
if [ -z "$changed_files" ]; then
  echo "No Python files have been modified."
  exit 0
fi

# Loop through each file
for file in $changed_files; do
  echo "Processing file: $file"
  
  # Revert the file to its previous state
  git checkout "$file"
  if [ $? -ne 0 ]; then
    echo "Failed to checkout file: $file"
    exit 1
  fi

  # Submit the file to Exercism
  exercism submit "$file"
  if [ $? -ne 0 ]; then
    echo "Failed to submit file: $file to Exercism."
    exit 1
  fi

  echo "Successfully submitted: $file"
done

echo "All changed Python files have been reverted and submitted."
