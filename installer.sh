#!/usr/bin/env bash
sudo apt update 1 > /dev/null 
# do-release-upgrade

sudo apt install -y python3 python3-dev
sudo apt install -y python3-pip python3-dev python3-setuptools

sudo pip3 install virtualenv virtualenvwrapper

echo -e "\nexport WORKON_HOME=$HOME/.virtualenvs" >> ~/.profile
echo "source /etc/bash_completion.d/virtualenvwrapper" >> ~/.profile
source ~/.profile

mkvirtualenv myenv








