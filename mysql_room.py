import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "mysql_room"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM mysql_rooms")

myrooms = mycursor.fetchall()

for room in myrooms:
    sql = "SELECT * FROM mysql_doors WHERE room_one = %s"
    adr = (room[4],)
    mycursor.execute(sql, adr)
    print(room)
    mydoors = mycursor.fetchall()
    for door in mydoors:
        print(door)

#mycursor.execute("CREATE TABLE mysql_room (name VARCHAR(50), description VARCHAR(255), length INT, width INT)")
#mycursor.execute("ALTER TABLE mysql_room ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#mycursor.execute("CREATE TABLE mysql_doors (door_id INT AUTO_INCREMENT PRIMARY KEY, wall VARCHAR(50), location INT, room_one INT, room_two INT)")
#mycursor.execute("RENAME TABLE mysql_room TO mysql_rooms")

'''
sql = "INSERT INTO mysql_rooms (name, description, length, width) VALUES (%s, %s, %s, %s)"
val = ("Entry", "Entrance", 5, 5)
mycursor.execute(sql, val)

sql = "INSERT INTO mysql_doors (wall, location, room_one, room_two) VALUES (%s, %s, %s, %s)"
val = [
    ('north', 4, 1, 2),
    ('west', 3, 2, 1)
]

mycursor.executemany(sql, val)
'''


#mydb.commit()