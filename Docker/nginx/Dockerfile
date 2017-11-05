# Set the base image
FROM ubuntu

# Author
LABEL Author="Kalinga Bhusan Ray"
LABEL E-Mail="kalinga-bhusan.ray@tu-ilmenau.de"
LABEL Desc="This is an image for nginx server "

#Update Repo
#RUN apt-get update

#Install nginx
#RUN apt-get install -y nginx

#Efficient building with a single layer
RUN apt-get update && \
    apt-get install -y nginx

#Working Dir
WORKDIR /

#Expose ports
EXPOSE 80


#Default command execution on container start up
#CMD service nginx start
CMD  /usr/sbin/nginx -g "daemon off;"

