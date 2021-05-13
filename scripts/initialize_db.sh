#!/bin/bash
set -x

TMP_DIR=$(mktemp -d 2>/dev/null || mktemp -d -t 'mytmpdir')
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# remove temp directory on exit
trap '{ rm -rf -- "$TMP_DIR"; }' EXIT

# download the mrds data set
curl --output "$TMP_DIR/mrds-csv.zip" https://mrdata.usgs.gov/mrds/mrds-csv.zip
cd $TMP_DIR && unzip mrds-csv.zip && sudo chown 10001:0 "$TMP_DIR/mrds.csv" && cd -

# if it exsists, remove the prior data directory
if [ -e $SCRIPT_DIR/../data/sqlserver/data ]; then
  sudo rm -rf $SCRIPT_DIR/../data/sqlserver/data
fi
mkdir -p $SCRIPT_DIR/../data/sqlserver/data
sudo chown 10001:0 $SCRIPT_DIR/../data/sqlserver/data

# start the database
export DATAFILE_PATH=$TMP_DIR/mrds.csv
export MSSQL_PATH=$SCRIPT_DIR/../data/sqlserver/data
export DATABASE_PASSWORD=$1
docker-compose -f $SCRIPT_DIR/../docker/docker-compose.init.yml up -d db

# pause to let database settle
echo "pausing to let the database settle"
sleep 20

# populate the database
$SCRIPT_DIR/../data/scripts/setup_database.py localhost 1433 SA "$DATABASE_PASSWORD"

# shut down db
docker-compose -f $SCRIPT_DIR/../docker/docker-compose.init.yml down 
