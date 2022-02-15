#!/bin/sh

# Setting up MSQL variables - change accordingly
DATABASE=subtiwiki_merge_v4
TABLE=Gene
USER=root
PASS=password
QUERY="SELECT * INTO OUTFILE '/usr/local/MySQLOutput/GeneTable.csv' FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n' FROM ${TABLE};"

# Running MySQL dump command
mysql --user ${USER} "-p${PASS}" -D ${DATABASE} -e "${QUERY}"

# Moving file to current directory
mv /usr/local/MySQLOutput/GeneTable.csv /Users/tiago/Desktop/AlphaFold2/Data/

# Note: Might need to change ownership of file to be readable