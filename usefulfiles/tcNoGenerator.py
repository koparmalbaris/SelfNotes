#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Code written by https://gist.github.com/canerbasaran/6334104
#
# Simple Turkish ID number generator
#
# Usage:
# wget https://raw.githubusercontent.com/koparmalbaris/tcnogenerator/main/tcNoGenerator.py
# for count in {1..10}; do python2 tcNoGenerator.py; done
#
#

from random import randint

def rastgele_tc():
    tcno = str(randint(100000000, 1000000000))
    list_tc = map(int, tcno)
    tc10 = (sum(list_tc[::2]) * 7 - sum(list_tc[1::2])) % 10
    return tcno + str(tc10) + str((sum(list_tc[:9]) + tc10) % 10)
    
print(rastgele_tc())
