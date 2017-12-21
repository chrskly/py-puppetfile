#!/usr/bin/env python

"""
Examples

forge "https://forgeapi.puppetlabs.com"

mod 'company-prod1',
  :git => "git@git.foobar:company/prod1.git",
  :ref => 'v1.2'

mod 'puppetlabs-stdlib', '4.17.1'

"""

import re

"""
This regex extracts
  - modulename
  - uri
  - ref
"""

r_string = \
    "^mod [\"'](?P<modulename>[a-zA-Z0-9\/\-\_]*)[\"']" + \
    "(," + \
    "(\n)?(\s+)?(\n)?" + \
    "(:git => \"(?P<uri>[a-zA-Z0-9:/\.\-@_]*)?\")?" + \
    ")?" + \
    "(," + \
    "(\n)?(\s+)?(\n)?" + \
    "(:ref => [\"'](?P<ref>[a-zA-Z0-9\.\-]*)[\"'])" + \
    ")?" + \
    "(.*?)"

module_match = re.compile(r_string, re.MULTILINE|re.DOTALL)

class reader:

    def __init__(self, fh):
        self.fh = fh
        self.output = {}

    def parse(self):
        """ parse Puppetfile """
        file_contents = "".join(self.fh.readlines())
        matches = module_match.finditer(file_contents)
        for m in matches:
            t_result = {}
            if m.group('uri'):
                t_result['uri'] = m.group('uri')
            if m.group('ref'):
                t_result['ref'] = m.group('ref')
            self.output["%s" % m.group('modulename')] = t_result
        return self.output

