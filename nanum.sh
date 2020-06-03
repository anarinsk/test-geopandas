#!/bin/bash

sudo sed -i 's/archive.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list
sudo apt-get update 
sudo apt-get install fonts-nanum*
sudo fc-cache -fv
python setting4pltfont.py

#cp /usr/share/fonts/truetype/nanum/Nanum* /opt/conda/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf/
#echo "font.family : NanumGothicCoding" >> /opt/conda/lib/python3.7/site-packages/matplotlib/mpl-data/matplotlibrc
echo "1. Nanum fonts are set!" &&
#echo "2. Append font.family to matplotrc"
echo "-----------------------"
