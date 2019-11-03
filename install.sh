#!/bin/bash
echo ================================================
echo ~~~~~~~~~~~~~~instaling scanme~~~~~~~~~~~~~~~~~~
echo ================================================
echo
echo installing python 3.6 virtual environment
virtualenv venv --python=python3.6
source venv/bin/activate
echo
echo ================================================
echo installing requirements
pip3 install -r requirements.txt
mkdir uploads
echo
echo ================================================
echo mysql username:
read sqluser
echo mysql password:
read -s sqlpass
echo mysql database:
read sqldb
echo session key:
read -s sessionkey
echo jwt key:
read -s jwtkey
echo email:
read email
echo email password:
read -s emailpass
touch schema.tmp.sql
python -c "open('schema.tmp.sql', 'w').write('create database if not exists $sqldb;\nuse $sqldb;\n'+open('schema.sql').read())"
echo creating database tables
cat schema.tmp.sql | mysql -u $sqluser -p
echo =================================================
rm schema.tmp.sql
touch config.py
echo writing configuration into config.py
python -c "open('config.py','w').write(open('config.orig').read().replace('<mysqlurl>','mysql://$sqluser:$sqlpass@localhost/$sqldb').replace('<sessionkey>','$sessionkey').replace('<jwtkey>','$jwtkey').replace('<email>','$email').replace('<emailpass>','$emailpass'))"
echo =================================================
echo ~~~~~~~~~~~~~~scanme installed~~~~~~~~~~~~~~~~~~~



