# sudo docker build -t kalinga/event-stream:v0.1 .  && sudo docker run -it --name event-stream kalinga/event-stream:v0.1 /bin/bash


# Set the base image
FROM python:3

# Author
LABEL Author="Kalinga Bhusan Ray"
LABEL E-Mail="kalinga-bhusan.ray@tu-ilmenau.de"
LABEL Desc="This is an image for event stream engiene"


#Efficient building with a single layer
RUN apt-get update && \
    apt-get install -y vim

ADD process_event_stream.py /

RUN pip install faust typing_extensions


#Expose ports
EXPOSE 80

#Default command execution on container start up
#CMD [ "python", "./process_event_stream.py" ]
