import pymongo

connect = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = connect["students"]
collection = mydb["student_info"]

loaddata = {"username": "KUI8", "password": "Hinll66", "firstname": "Kevin", "email": "Kbomb10@aol.com" 
"dob": "6/7/1989" "zip": "8090"}

x = collection.insert_one(loaddata)