#https://github.com/sequenceiq/hadoop-docker/blob/2.7.1/Dockerfile
# This give Hadoop 2.7.1
# Apache Hadoop from 2.7.x to 2.x support Java 7 and 8
# https://cwiki.apache.org/confluence/display/HADOOP/Hadoop+Java+Versions
FROM sequenceiq/hadoop-docker:2.7.1

MAINTAINER Kalinga Bhusan Ray <mail.kalinga@gmail.com>

RUN hostname
RUN pwd

RUN mkdir /docker

#COPY  ../../../../../vagrant/scripts/common.sh /docker/scripts/
#COPY  ../../../../../vagrant/scripts/stop-hadoop.sh /docker/scripts/

COPY  ./scripts /docker/
RUN ls /docker