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

Remove all stopped/Exited containers
docker ps -aq --no-trunc | xargs docker rm

List all Exited containers
docker ps -aq -f status=exited

Filter op based on a condition
docker ps -a -f name="loving*"

Docker Copy without volume plugin
docker cp 1.txt 2cd4df5495b0:/
docker cp  2cd4df5495b0:/2.txt .

Check connectivity from within the docker container/image creation process
docker run busybox nslookup google.com 

Solution if there is a DNS issue. Put below command o/p to /etc/docker/daemon.json 
Find out the primary and secondary DNS server addresses:
nmcli dev show | grep 'IP4.DNS'

Credit stackoverflow post and Robin Winslow's original blog.

