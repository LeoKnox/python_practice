import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="dba"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE characters (name VARCHAR(255), class VARCHAR(255))")