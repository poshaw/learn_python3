#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

def main(args):
	print("hello world!")
	print("you are running python version: {}!".format(sys.version))
	return 0

if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))
