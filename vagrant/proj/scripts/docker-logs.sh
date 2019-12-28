#/usr/bin/bash
rm docker.log

# Remove all dangling images that are not required
# Docker warns you if any containers exist that are using these untagged images.
#https://docs.docker.com/engine/reference/commandline/images/#filtering

docker rmi $(docker images -f "dangling=true" -q) 

echo "$(date)" >> docker.log
docker images >> docker.log
docker ps >> docker.log