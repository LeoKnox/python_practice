import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="dba"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE characters (name VARCHAR(255), class VARCHAR(255))")

#mycursor.execute("ALTER TABLE characters ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#sql = "INSERT INTO characters (name, class) VALUES (%s, %s)"
#val = ("Aelien", "Fighter")

#mycursor.execute(sql, val)

'''
val = [
    ("Eveehi", "Mage"),
    ("Xingu", "Rogue")
]
'''

#mycursor.executemany(sql, val)

#mydb.commit()

mycursor.execute("SELECT * FROM characters")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

mycursor.execute("SELECT name FROM characters")

myresult = mycursor.fetchone()

print(myresult)

print(mycursor.rowcount, " number of rows")