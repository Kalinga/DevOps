# Set the base image
FROM nginx

# Author
LABEL Author="Kalinga Bhusan Ray"
LABEL E-Mail="kalinga-bhusan.ray@tu-ilmenau.de"
LABEL Desc="This is an image for nginx proxy server for serving node.js application request"

COPY etc-nginx-sites-available-default /etc/nginx/sites-available/default

COPY html /usr/share/nginx/html

#Working Dir
WORKDIR /

#Expose ports
EXPOSE 80

#Default command execution on container start up
#CMD service nginx start
CMD  /usr/sbin/nginx -g "daemon off;"