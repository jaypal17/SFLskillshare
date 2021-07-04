import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="dbuser1",
  password="********",
  database="students"
)

mycursor = mydb.cursor()

sql = "INSERT INTO student_info (username, password, firstname, email, dob, zip) VALUES (%s, %s)"
val = [
  ("LN1J", "Xmmrtuv1877", "Larry", "larry1zp@yahoo.com", "8/16/1993", "1991"),
  ("MKT8", "Jujjy67i", "Michael", "Mzoo18@aol.com", "1998-09-09", "1909"),
  ("F9OP", "Ki78unma", "Frank", "Ff8900@gmail.com", "1991-10-4", "8818"),
  ("RIT7", "TxzY1ull", "Rachel", "RachelRay90@yahoo.com", "1990-09-19", "0992"),
  ("Q22y", "Z11EWNV", "Quinn", "Qqui3t8@aol.com", "1993-05-12", "1161"),
  ("BTE4", "Yuy81te", "Blake", "BDizz13@gmail.com", "1990-04-11", "5155"),
  ("NTP5", "Neewe78", "Neil", "ZeroDarkling1@yahoo.com", "1994-06-16", "1021"),
  ("PQV6", "Zooil68", "Pual", "Pmn16@aol.com", "1995-07-14", "0990"),
  ("JI7D", "Vuvv12", "James", "JamesJames8@gmail.com", "1992-06-09", "8776"),
  ("TWq2", "Bnev18", "Tyler", "Tyty8081@yahoo.com", "1993-05-14", "2180")
]
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
