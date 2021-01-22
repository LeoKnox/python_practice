import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "mysql_room"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE mysql_room (name VARCHAR(50), description VARCHAR(255), length INT, width INT)")