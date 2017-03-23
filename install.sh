#!/usr/bin/env bash

sudo cp src/zajeb.py /bin/zajeb
sudo cp src/przyjeb.sh /bin/przyjeb
sudo cp src/wyjeb.py /bin/wyjeb
sudo cp src/dojeb.py /bin/dojeb

sudo mkdir /etc/pojeb
sudo mkdir /etc/pojeb/wyjeb.d

sudo chmod ugo+rx /bin/zajeb
sudo chmod ugo+rx /bin/przyjeb
sudo chmod ugo+rx /bin/wyjeb
sudo chmod ugo+rx /bin/dojeb
