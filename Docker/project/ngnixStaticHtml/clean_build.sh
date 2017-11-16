docker stop iamkalinga.com
docker ps -a

docker ps -aq -f status=exited |  xargs docker rm
docker rmi kalinga/mywebsite:v0.1
docke images

docker build -t kalinga/mywebsite:v0.1 .
docker run -itd  --name=iamkalinga.com -p 8081:80  kalinga/mywebsite:v0.1

docker ps -a
docker exec -it iamkalinga.com bash