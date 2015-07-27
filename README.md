# lpthw
My solutions to Learn Python The Hard Way exercises.     

[Git Hook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) added to run [flake8](https://pypi.python.org/pypi/flake8) on .py files, pre-commit.

```bash
#!/bin/sh

# Auto-check for PEP8
FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -e '\.py$')

if [ -n "$FILES" ]; then
    flake8 -r $FILES
fi
```

(Thanks to [signal0](http://signal0.com/2012/07/11/syntax_pep8_checking_before_committing_in_git.html).)
