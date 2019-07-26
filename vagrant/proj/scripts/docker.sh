#/usr/bin/bash

# docker provision installs Docker version 18.06.3-ce, build d7080c1
# With that version, there seems to be a problem
# https://forums.docker.com/t/ubuntu-16-04-docker-run-error-solved/69093

docker -v 

sudo add-apt-repository    "deb [arch=amd64] https://download.docker.com/linux/ubuntu    $(lsb_release -cs)   stable"
sudo apt-get update

# https://docs.docker.com/install/linux/docker-ce/ubuntu/
# The Docker Engine - Community package is now called docker-ce
# Docker Engine - Community uses the overlay2 storage driver by default. 
sudo apt-get install -y   --force-yes docker-ce=18.06.1~ce~3-0~ubuntu

docker -v
 
