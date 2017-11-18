Build image:
docker build -t kalinga/nodeapp_nginx:v0.1 .
docker build -t kalinga/nodeapp:v0.1 .

Running the image:
docker run -d --name="nodejs" -p 8081:8081 kalinga/nodeapp:v0.1
docker run -d --name="nodeapp_nginx" -p 8080:80 --link nodejs:nodejs kalinga/nodeapp_nginx:v0.1

docker exec  -it nodeapp_nginx bash
docker exec  -it nodeapp bash


docker rm nodeapp nodeapp_nginx

ip addr show
apt-get install iproute2
apt-get install iputils-ping

/etc/nginx/nginx.conf -> include /etc/nginx/sites-enabled/*;
/etc/nginx/sites-enabled/default -> /etc/nginx/sites-available/default

http://localhost:8080/iamkalinga.html
