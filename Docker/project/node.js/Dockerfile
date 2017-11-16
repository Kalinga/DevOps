# Set the base image
FROM kalinga/nodeapp:v0.1

# Author
LABEL Author="Kalinga Bhusan Ray"
LABEL E-Mail="kalinga-bhusan.ray@tu-ilmenau.de"
LABEL Desc="This is an image for node.js app "

#Efficient building with a single layer
#RUN apt-get update && \
#	apt-get install -y curl && \
#	curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
#    apt-get install -y nodejs


RUN which node && \
	node --version

COPY hello.js /root/nodejs_app/hello.js

#Working Dir
WORKDIR /

#Expose ports
EXPOSE 80

#Default command execution on container start up
#CMD service nginx start
#CMD  /usr/sbin/nginx -g "daemon off;"

