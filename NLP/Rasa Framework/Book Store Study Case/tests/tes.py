import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="chatbotdb"
)

mycursor = mydb.cursor()
sql = "Insert into customers VALUES (%s, %s, %s, %s, %s)"
val = (0, 'Mohammad Aufar', 8177413292, 'dummy@email.com', 'aaaaa')
mycursor.execute(sql, val)
mydb.commit()