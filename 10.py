#!/bin/python
# -*- coding: utf-8 -*-

import sys

with open(sys.argv[1], "r", encoding="utf-8") as f:
    lines = f.readlines()

print(len(lines))
