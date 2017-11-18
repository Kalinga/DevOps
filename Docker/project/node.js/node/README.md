Can be used individually or in combination with nginx

Build image:
docker build -t kalinga/nodeapp:v0.1 .

Running the image:
docker run -d --name="nodejs" -p 8081:8081 kalinga/nodeapp:v0.1

docker exec  -it nodeapp bash

ip addr show
apt-get install iproute2
apt-get install iputils-ping