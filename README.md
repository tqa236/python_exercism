# Python Exercism

Solutions for Python track on Exercism

TODO:

- Try uv for dependency management
- Solve sgf parsing
- Configure ruff
- Optimize palindrome
- Make a reasonable linter set on CI with superlinter

```bash
ruff --exclude="*_test.py","*_data.py" --select ALL --preview . --ignore=D102,CPY001,ANN101
ruff list-ops/list_ops.py --select ALL --target-version="py311" --fix
```
