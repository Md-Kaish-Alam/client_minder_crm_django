# Install mysql
# pip install mysql
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='kaishalam',
    passwd='Nuwaish@1511'
)

# prepare a cursor object

cursorObject = dataBase.cursor()

# create a database

cursorObject.execute("CREATE DATABASE CLIENT_MINDER")

print("Database created !")