#!/bin/bash
#
# This creates a backup of both the site and the database.
echo "Backing up website files."
mkdir -p ./bak/
MYDATESTR=$(date +"%Y-%m-%d")
MYFILENAME="../bak/silica_files_$MYDATESTR.tgz"
tar cfz $MYFILENAME * --exclude=log --exclude=silica-gel.org
echo "Backing up database. Enter sudo password."
sudo MYDATESTR=$MYDATESTR su postgres -c 'pg_dump silica > /tmp/silica_$MYDATESTR.sql'
sudo MYDATESTR=$MYDATESTR su postgres -c 'gzip -9 /tmp/silica_$MYDATESTR.sql'
sudo MYDATESTR=$MYDATESTR chown xangis:xangis /tmp/silica_$MYDATESTR.sql.gz
mv /tmp/silica_$MYDATESTR.sql.gz ../bak/
ls -l $MYFILENAME
ls -l ../bak/silica_$MYDATESTR.sql.gz
