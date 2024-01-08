# Python Exercism

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8fd44be5d9984cb4b963b176a251494f)](https://www.codacy.com/app/tqa236/python_exercism?utm_source=github.com&utm_medium=referral&utm_content=tqa236/python_exercism&utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/tqa236/python_exercism/badge.svg?branch=main)](https://coveralls.io/github/tqa236/python_exercism?branch=main)
[![codecov](https://codecov.io/gh/tqa236/python_exercism/branch/main/graph/badge.svg)](https://codecov.io/gh/tqa236/python_exercism)

Solutions for Python track on Exercism

TODO:

-   Try poetry for dependency management
-   Solve sgf parsing
-   Configure ruff
-   Optimize palindrome

```bash
ruff --exclude="*_test.py","*_data.py" --select ALL --preview . --ignore=D102,CPY001,ANN101
ruff list-ops/list_ops.py --select ALL --target-version="py311" --fix
```
