#!/usr/bin/env python
# coding=UTF-8
"""
zajeb: make target directory into a .jeb package

Usage:

    zajeb directory-name

Effect:

    creates a file called directory-name.jeb in current working directory
"""
from __future__ import print_function, absolute_import, division
import zipfile
import os
import sys

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       arcname=os.path.relpath(os.path.join(root, file), sys.argv[1]))

if __name__ == '__main__':

    if len(sys.argv[1]) < 1:
        print('''RTFM: https://github.com/smok-serwis/pojeb
Pass name of directory to jeb.''')
        sys.exit(1)

    if not os.path.exists(os.path.join(sys.argv[1], 'dojeb')):
        print('''RTFM: cannot make package without dojeb''')
        sys.exit(1)

    zipf = zipfile.ZipFile(sys.argv[1]+'.jeb', 'w', zipfile.ZIP_DEFLATED)
    zipdir(sys.argv[1], zipf)
    zipf.close()
