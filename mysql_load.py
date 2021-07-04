import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="dbuser1",
  password="********",
  database="students"
)

mycursor = mydb.cursor()

sql = "INSERT INTO student_info (username, password, firstname, email, dob, zip)"
VALUES (%s, %s)"
val = ("LN1J", "Xmmrtuv1877", "Larry", "larry1zp@yahoo.com", "8/16/1993", "1991")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
