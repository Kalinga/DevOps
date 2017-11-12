First, add the GPG key for the official Docker repository to the system:

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
Add the Docker repository to APT sources:

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
Next, update the package database with the Docker packages from the newly added repo:

sudo apt-get update

Make sure you are about to install from the Docker repo instead of the default Ubuntu 16.04 repo:

apt-cache policy docker-ce

Finally, install Docker:

sudo apt-get install -y docker-ce

Docker should now be installed, the daemon started, and the process enabled to start on boot.
Check that it's running:

sudo systemctl status docker

Docker with out sudo

Create the docker group.

sudo groupadd docker

Add your user to the docker group.
sudo usermod -aG docker $USER


Check connectivity from within the docker container/image creation process
docker run busybox nslookup google.com 

Solution if there is a DNS issue. Put below command o/p to /etc/docker/daemon.json 
Find out the primary and secondary DNS server addresses:
nmcli dev show | grep 'IP4.DNS'

Credit stackoverflow post and Robin Winslow's original blog.

Container Connection Mode
	Detached Mode For running apps within the Container
	Root User Mode For trouble shooting inside the container


[SWARM] Docker swarm is a cluster of machine running docker which provide
scalable and realiable  platform to run many containers.

Docker Machine:
curl -L https://github.com/docker/machine/releases/download/v0.13.0/docker-machine-`uname -s`-`uname -m` >/tmp/docker-machine &&
chmod +x /tmp/docker-machine &&
sudo cp /tmp/docker-machine /usr/local/bin/docker-machine

Install ui-for-docker
docker run -d -p 9000:9000 --privileged -v /var/run/docker.sock:/var/run/docker.sock uifd/ui-for-docker
localhost:9000 in the browser shows the UI

Docker daemon default config file cat /etc/default/docker
Another place for it: /etc/docker/daemon.json

By default the docker daemon listens on local var/run/docker.sock

systemd is the init process for modern Lunix based OS like Ubuntu
systemctl <service name> status gives the status of the service
	
