# Learn Python 3
## Overhead
This exersise assumes you are using linux

Make sure python is installed
``` bash
$ python --version
```

We need to know where python is installed for the "sh-bang"
``` bash
$ which python
```

For me it's at /usr/bin/python

Clone this git repository to a local machine
``` bash
$ git clone git@github.com:poshaw/learn_python3.git
```

Make change to some files
``` bash
$ nvim README.md
```

Commit the changes
``` bash
$ git commit -a -m $(date +%Y%m%d_%H%M)
```

And push these changes back to your repo on github
``` bash
$ git push -u origin main
```

## Hello World
``` python
#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

def main(args):
	print("hello world!")
	print("you are running python version: {}!".format(sys.version))
	return 0

if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))
```
