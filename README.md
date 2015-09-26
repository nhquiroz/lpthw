# lpthw

[![Code Climate](https://codeclimate.com/github/nhquiroz/lpthw/badges/gpa.svg)](https://codeclimate.com/github/nhquiroz/lpthw) 
[![Code Health](https://landscape.io/github/nhquiroz/lpthw/master/landscape.svg?style=flat)](https://landscape.io/github/nhquiroz/lpthw/master) 
[![Code Issues](http://www.quantifiedcode.com/api/v1/project/cbd7dcc8bdb04519a8d247069bc9e6dc/badge.svg)](http://www.quantifiedcode.com/app/project/cbd7dcc8bdb04519a8d247069bc9e6dc)

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


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/nhquiroz/lpthw/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

