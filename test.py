#!/usr/bin/env python

import puppetfile

with open('Puppetfile', 'r') as mypuppetfile:
    pfr = puppetfile.reader(mypuppetfile)
    modules = pfr.parse()

print modules
