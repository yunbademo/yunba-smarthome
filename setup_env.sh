#!/usr/bin/env bash

set e

sudo apt-get update
#sudo apt-get install build-essential
sudo apt-get install python-dev
sudo apt-get install python-pip
#sudo apt-get install python-rpi.gpio

#sudo apt-get install git
git clone https://github.com/adafruit/Adafruit_Python_DHT.git

cd Adafruit_Python_DHT
sudo python setup.py install
cd ..

sudo pip install -U socketIO-client==0.5.5

sudo apt-get install mplayer

