#!/usr/bin/python
# coding=UTF-8
"""
dojeb: install a .jeb package

Pass path to the zip as the argument.
"""
from __future__ import print_function, absolute_import, division
import sys
import tempfile
import os
import shutil
import os.path
import zipfile


if __name__ == '__main__':
    if len(sys.argv[1]) < 1:
        print('''RTFM: https://github.com/smok-serwis/pojeb
Pass a .jeb file to install''')

    # what is the package named?
    pkname = os.path.splitext(os.path.split(sys.argv[1])[1])[0]

    cur_wd = os.getcwd()

    # unzip to a temporary directory. Our tempdirs are the BEST
    temp_d = tempfile.mkdtemp()
    zf = zipfile.ZipFile(sys.argv[1])
    zf.extractall(temp_d)

    # Fucking right, execute install
    os.chdir(temp_d)
    os.chmod('dojeb', 500)
    rc = os.system('./dojeb')

    if rc == 0:
        # huge success
        if os.path.exists('wyjeb'):
            os.chmod('wyjeb', 500)
            shutil.copy('wyjeb', os.path.join('/etc/pojeb/wyjeb.d/', pkname))
            print(u"Installed all right :-D")
        else:
            print(u"Installed OK, but you can't uninstall it ヽ(´ー｀)ノ")
    else:
        print(u"Install script exited with RC %s (╯°□°）╯︵ ┻━┻")

    # fucking wipe the tempdir. It's gonna be awesome
    os.chdir(cur_wd)
    shutil.rmtree(temp_d, ignore_errors=True)

    # thank you for being an awesome user of pojeb
    sys.exit(rc)
