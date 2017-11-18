# Set the base image
FROM nginx

# Author
LABEL Author="Kalinga Bhusan Ray"
LABEL E-Mail="kalinga-bhusan.ray@tu-ilmenau.de"
LABEL Desc="This is an image for nginx proxy server for serving \
			request meants for node.js application request"

RUN apt-get update && apt-get -y install \
	curl iproute2 iputils-ping

COPY config/nginx.conf /etc/nginx/conf.d/default.conf

COPY html /usr/share/nginx/html

#Working Dir
WORKDIR /

#Expose ports
EXPOSE 80

#Default command execution on container start up
#CMD service nginx start
CMD  /usr/sbin/nginx -g "daemon off;"