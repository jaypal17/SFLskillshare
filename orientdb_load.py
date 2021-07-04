import pyorient
#Create connection 
client = pyorient.OrientDB("localhost", 2424) 
session_id = client.connect( "root", "Blue1234" )
 
#open databse 
client.db_open("student_records", "root", "Blue1234") 

#insert record 
client.command("INSERT INTO Records ('username', 'record', 'gpa', 'studentID', 'phoneNum') VALUES('KUI8', '0001', '%3.5', '2001', '123-865-9901')") 
