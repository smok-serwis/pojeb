#!/usr/bin/env bash
cp src/zajeb.py /bin/zajeb
cp src/przyjeb.sh /bin/przyjeb
cp src/wyjeb.py /bin/wyjeb
cp src/dojeb.py /bin/dojeb

mkdir /etc/pojeb
mkdir /etc/pojeb/wyjeb.d

chmod ugo+rx /bin/zajeb
chmod ugo+rx /bin/przyjeb
chmod ugo+rx /bin/wyjeb
chmod ugo+rx /bin/dojeb
