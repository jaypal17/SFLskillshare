#!/bin/sh
#Get latest packages
sudo apt-get update
#Install OrientDB
sudo wget https://s3.us-east-2.amazonaws.com/orientdb3/releases/3.0.34/orientdb-3.0.34.tar.gz -O orientdb-community-3.0.34.tar.gz
#unzip
tar -zxvf orientdb-community-3.0.31.tar.gz