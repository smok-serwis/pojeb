#!/usr/bin/env bash

JEBNAME=$(basename "$2")
scp "$2" "$1:$JEBNAME"
ssh "$1" <<ENDSSH
if [ ! -d "/etc/pojeb" ]; then
    wget -O - https://github.com/smok-serwis/pojeb/raw/master/jebac-to | sudo bash
fi
sudo dojeb $JEBNAME ${@:3}
rm -f $JEBNAME
ENDSSH
