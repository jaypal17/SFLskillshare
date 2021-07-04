import mysql.connector
import pymongo

# Extracted data
all_data = {}

# Extract from Mysql
try:
    mysqlconn = mysql.connector.connect(
        host="localhost",
        user="dbuser1",
        password="Blue1234",
        database="students")

    sql_select_query = "select * from student_info"
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    # fetch result
    record = cursor.fetchall()

    for row in record:
        print("username = ", row[0], )
        print("password = ", row[1])
        print("firstname = ", row[2])
        print("email = ", row[3])
        print("dob = ", row[4])
        print("zip = ", row[5])
        row.append(all_data)


except mysql.connector.Error as error:
    print("Failed to get record from MySQL table: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

# Convert zip data from all data to int
for i in all_data["zip"]:
    to_int = int(i)

# Mongo load
try:
    connect = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = connect["students"]

    collection = mydb["student_info"]
    # loads data into collection
    loaddata = all_data

    x = collection.insert_one(loaddata)

except pymongo.connector.Error as error:
    print("Failed to insert data")
