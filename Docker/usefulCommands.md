location for docker related data /var/lib/docker/*

docker version
docker help
docker images

docker run kalinga/nginx:v0.1
"Config": {
            "AttachStdin": false,
            "AttachStdout": true,
            "AttachStderr": true,
          }

docker run -d kalinga/nginx:v0.1
"Config": {
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
          }

Building an image
-t is the tag and . indicates Dockerfile present in the CWD
docker build -t kalinga/mywebsite:v0.1 .
docker run -p 8081:80  kalinga/mywebsite:v0.1

docker run -p 8081:80 kalinga/nginx:v0.1
docker run -d -p 8081:80 kalinga/nginx:v0.1
docker run -it -d -p 8081:80 kalinga/nginx:v0.1

Can get a terminal to the above running container
docker exec -it <<71eb39874dc1>> bash

8081 port on the Host
80 port from the running container

Inspect IP address
docker inspect --format '{{.NetworkSettings.IPAddress}}' 914
docker inspect -f '{{.State.Pid}}' "<container name>"
   

docker run -d -P nginx
With option -P(Capital P), container can bind to a free port in the range
32768-65000 to the exposed port of the container

Check Port
docker port <container id>
sample op. 80/tcp [port in Container]-> 0.0.0.0:32768 [port in Host]

Checking the local web server
curl http://$(hostname -i):32768

docker ps : All active containers
docker ps -a : All active/inactive containers
docker search 'hello' searches in the docker hub
	
Remove all stopped/Exited containers
docker ps -aq --no-trunc | xargs docker rm

List all Exited containers
docker ps -aq -f status=exited

Filter op based on a condition
docker ps -a -f name="loving"

Docker Copy without volume plugin
docker cp 1.txt 2cd4df5495b0:/
docker cp  2cd4df5495b0:/2.txt .

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

docker run -it -v myshared_path_from_host:/my_mounted_path_in_container image_name

We can run docker on different sockets like tcp, unix and fd
Below command a tcp port is used and 2375 is used for unencryption communication

dockerd -H tcp://127.0.0.1:2375

When we use above command normal command `dockerimages` will give error
and we need to use docker -H localhost:2375 images.

Link:
docker run -d --name redis1 redis
docker run -it --name redisClient busybox

Networking:
docker run -it --net=bridge --name=bridge busybox
ip addr gives => inet 172.17.0.2/16 scope global eth0 (bridge subnet)

docker run -it --net=none --name=none busybox
ip addr
lo: <LOOPBACK,UP,LOWER_UP>  (Only Loop back entry)

docker run -it --net=host --name=host busybox
ip addr
List all interfaces as Host

Restrict Connectivity to outside World
--iptable=false
--ip-forward=false
Have these parameters in /etc/default/docker

Use of pipework can introduce a network interface using that 
containers can communicate among them

Docker HUB login
docker login

