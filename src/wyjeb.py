#!/usr/bin/python
# coding=UTF-8
"""
dojeb: install a .jeb package

Pass path to the zip as the argument.
"""
from __future__ import print_function, absolute_import, division
import sys
import os
import os.path


if __name__ == '__main__':
    if len(sys.argv[1]) < 1:
        print('''RTFM: https://github.com/smok-serwis/pojeb
Pass a package name to uninstall''')

    uninst_script = os.path.join('/etc/pojeb/wyjeb.d', sys.argv[1])

    if not os.path.exists(uninst_script):
        print(u'Error: either your package is not installed or does not support uninstall.')
        sys.exit(1)

    os.chmod(uninst_script, 644)
    rc = os.system(uninst_script)
    os.unlink(uninst_script)
