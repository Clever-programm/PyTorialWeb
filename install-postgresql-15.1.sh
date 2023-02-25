#!/bin/bash

local_db_handler="./utils/db/postgres"
logfile=$local_db_handler/postgresql/logfile.txt

touch $logfile

echo logs at $logfile

echo creating work directory
mkdir -p $local_db_handler

echo downloading postgresql
curl --create-dir --output $local_db_handler/postgres.tar.gz https://ftp.postgresql.org/pub/source/v15.1/postgresql-15.1.tar.gz > $logfile

echo extracting postgresql
tar -xvf $local_db_handler/postgres.tar.gz -C $local_db_handler > $logfile


echo creating symbolic link
ln -s postgresql-15.1 $local_db_handler/postgresql > $logfile


echo moving to the work directory
cd $local_db_handler/postgresql > $logfile


echo configure
./configure > $logfile


echo install
make install -f GNUmakefile > $logfile


