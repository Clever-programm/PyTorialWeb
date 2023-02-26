#!/bin/bash

local_db_handler=$(pwd)/utils/db/postgres
# logfile=$local_db_handler/postgresql/logfile.txt
# templog=$(pwd)/logfile.txt


# echo $logfile, $templog
# touch $logfile
# touch $templog


# echo logs at $logfile


echo creating work directory
mkdir -p $local_db_handler


echo downloading postgresql
#curl --create-dir --output $local_db_handler/postgres.tar.gz https://ftp.postgresql.org/pub/source/v15.1/postgresql-15.1.tar.gz # > $templog


echo extracting postgresql
tar -xvf $local_db_handler/postgres.tar.gz -C $local_db_handler # > $templog


echo creating symbolic link
ln -s postgresql-15.1 $local_db_handler/postgresql # > $templog


echo moving to the work directory
cd $local_db_handler/postgresql


echo configure
./configure --without-zlib # > $templog


echo make install
make install -f GNUmakefile # > $templog

echo post configure
adduser postgres # > $templog

mkdir -p /usr/local/pgsql/data
chown postgres /usr/local/pgsql/data # > $templog

su - postgres # > $templog

/usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data # > $templog

/usr/local/pgsql/bin/pg_ctl -D /usr/local/pgsql/data -l logfile start # > $templog

/usr/local/pgsql/bin/createdb test # > $templog

/usr/local/pgsql/bin/psql test # > $templog


# cat $templog > $logfile

