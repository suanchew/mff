#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y git python-dev python-pip python-virtualenv bpython ipython sqlite3 libxml2-dev libxslt1-dev libffi-dev nodejs libssl-dev postgresql-client postgresql-doc-9.3 postgresql postgresql-contrib postgresql-server-dev-9.3
sudo -u postgres createuser root -s
sudo -u postgres createuser vagrant -s
createdb vagrant
sudo pip install psycopg2
