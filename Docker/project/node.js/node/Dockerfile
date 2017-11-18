# Set the base image
FROM debian

# Author
LABEL Author="Kalinga Bhusan Ray"
LABEL E-Mail="kalinga-bhusan.ray@tu-ilmenau.de"
LABEL Desc="This is an image for node.js app "

#Efficient building with a single layer
#RUN apt-get update && \
#	apt-get install -y curl && \
#	curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
#    apt-get install -y nodejs

RUN apt-get update && apt-get -y install \
    gnupg curl \
    iproute2 \
	iputils-ping \
	python build-essential

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get -y install nodejs

COPY src/ /root/nodejs_app/

#Working Dir
WORKDIR /

#Expose ports
EXPOSE 8081

# Run app using node
CMD ["node", "/root/nodejs_app/hello.js"]

