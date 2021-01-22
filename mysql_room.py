import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "mysql_room"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE mysql_room (name VARCHAR(50), description VARCHAR(255), length INT, width INT)")
#mycursor.execute("ALTER TABLE mysql_room ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

mycursor.execute("CREATE TABLE mysql_doors (door_id INT AUTO_INCREMENT PRIMARY KEY, wall VARCHAR(50), location INT, room_one INT, room_two INT)")
mycursor.execute("RENAME TABLE mysql_room TO mysql_rooms")