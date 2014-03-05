#! /usr/bin/env bash

sudo apt-get update

sudo apt-get install -y python-pip &&
sudo apt-get install -y build-essential &&

sudo apt-get install -y -f libqt4-dev &&
#sudo apt-get build-dep libqt4-dev

sudo apt-get install -y gperf bison &&
sudo apt-get install -y libxcb1 libxcb1-dev libx11-xcb1 libx11-xcb-dev libxcb-keysyms1 libxcb-keysyms1-dev libxcb-image0 libxcb-image0-dev libxcb-shm0 libxcb-shm0-dev libxcb-icccm4 libxcb-icccm4-dev libxcb-sync0 libxcb-sync0-dev libxcb-xfixes0-dev libxrender-dev libxcb-shape0-dev &&

sudo apt-get install -y mongodb mongodb-dev &&
sudo apt-get install -y python-dev &&
#sudo pip install -U numpy &&
sudo apt-get install -y python-numpy &&

sudo pip install -U networkx &&

sudo apt-get install -y libqt4-opengl &&
sudo apt-get install -y python-qt4-gl &&
sudo apt-get install -y python-pyside.qtopengl &&

sudo apt-get install -y libfreetype6 libfreetype6-dev -y &&
sudo apt-get install -y python-vtk &&

#sudo apt-get install -y python-pyqt python-pyqt-dev &&
sudo apt-get install -y python-qt4 python-qt4-dev &&
sudo apt-get install -y python-matplotlib &&
sudo apt-get install -y python-suds &&
sudo apt-get install -y python-support