import pymongo

connect = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = connect["students"]
#creates collection
collection = mydb["student_info"]
index_name = 'my_index'
collection.create_index(name=index_name, unique=False)
#loads data into collection
loaddata = [{"username": "KUI8", "password": "Hinll66", "firstname": "Kevin", "email": "Kbomb10@aol.com", 
"dob": "6/7/1989", "zip": "8090"},
            {"username": "JMZ0", "password": "GuIl90", "firstname": "Jimmy", "email": "jimboy8@yahoo.com", "dob": "4/14/2001", "zip": "8781"},
            {"username": "VAW4", "password": "Bnb18z", "firstname": "Valerie", "email": "Valgirl18@gmail.com", "dob": "5/9/1999", "zip": "2102"},
            {"username": "RNM3", "password": "Tuillq2", "firstname": "Raymond", "email": "Rayray5@aol.com", "dob": "7/9/2002", "zip": "2303"},
            {"username": "GH6Z", "password": "VCik3", "firstname": "Greg", "email": "Hotsauce6@aol.com", "dob": "2/24/1998", "zip": "4144"},
            {"username": "Ino7", "password": "Si37k", "firstname": "Ian", "email": "Isoccer@gmail.com", "dob": "4/23/1999", "zip": "5241"},
            {"username": "WVB3", "password": "Zinh16", "firstname": "Wendy", "email": "Wendy.Smith@gmail.com", "dob": "6/22/2002", "zip": "6166"},
            {"username": "HBK9", "password": "WasL45", "firstname": "Harvey", "email": "Hball8@yahoo.com", "dob": "3/30/2000", "zip": "8181"},
            {"username": "ENT1", "password": "LiCnk88", "firstname": "Edward", "email": "em1888@gmail.com", "dob": "4/18/2001", "zip": "3034"},
            {"username": "Z6GH", "password": "MooZX98", "firstname": "Zachary", "email": "ZJune17@yahoo.com", "dob": "6/17/2002", "zip": "5059"},           

x = collection.insert_many(loaddata)
