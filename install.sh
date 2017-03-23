#!/usr/bin/env bash

sudo cp src/zajeb.py /usr/bin/zajeb
sudo cp src/przyjeb.sh /usr/bin/przyjeb
sudo cp src/wyjeb.py /bin/wyjeb
sudo cp src/dojeb.py /bin/dojeb

sudo mkdir -p /etc/pojeb
sudo mkdir -p /etc/pojeb/wyjeb.d

sudo chmod ugo+rx /usr/bin/zajeb
sudo chmod ugo+rx /usr/bin/przyjeb
sudo chmod ugo+rx /bin/wyjeb
sudo chmod ugo+rx /bin/dojeb
