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

sql = "INSERT INTO characters (name, class) VALUES (%s, %s)"
val = ("Aelien", "Fighter")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, " number of rows")