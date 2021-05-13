#!/bin/bash
set -x

TMP_DIR=$(mktemp -d 2>/dev/null || mktemp -d -t 'mytmpdir')
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# start the database
export MSSQL_PATH=$SCRIPT_DIR/../data/sqlserver/data
export DATABASE_PASSWORD=$1
export APP_PATH=$SCRIPT_DIR/../web
docker-compose -f $SCRIPT_DIR/../docker/docker-compose.yml down 
