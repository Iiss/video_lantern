#!/bin/sh
# setup.sh
# install lantern dependencies & provide autorun setup
mkdir -p playlist
sudo apt-get update
sudo apt-get install omxplayer
sudo nano /etc/rc.local