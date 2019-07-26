#/usr/bin/bash

#https://cwiki.apache.org/confluence/display/HADOOP/Hadoop+Java+Versions
#Apache Hadoop from 2.7.x to 2.x support Java 7 and 8
version=($1)
echo Requested java open jdk version  is $1
if [ $version -eq 8 ]
then
        sudo add-apt-repository -y ppa:openjdk-r/ppa
        sudo apt-get update
        sudo apt-get install -y openjdk-8-jdk
else
        sudo apt-get update
        sudo apt-get install -y openjdk-7-jdk
fi

java -version
javac -version