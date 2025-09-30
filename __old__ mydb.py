


import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Moy_Password123',
)


# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create the database
cursorObject.execute("CREATE DATABASE fedeco")

print("Finished.")