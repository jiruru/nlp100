# -*- coding: utf-8 -*-
import sys

sys.stdout.write(open("./hightemp.txt").read().replace('\t', ' '))
