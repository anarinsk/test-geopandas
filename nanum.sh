#!/bin/bash

sudo sed -i 's/archive.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list
sudo apt-get update 
sudo apt-get install fonts-nanum*
sudo fc-cache -fv

echo "Nanum fonts are set!" &&
echo "-----------------------"