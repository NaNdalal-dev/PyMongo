import pymongo

client = pymongo.MongoClient("localhost",27017)

mydb = client["MyDataBase"]

#Creating Customers database 
mycollection = mydb["CustomersData90"]

myList = [
			{"name":"john","address": "Park Lane 38"},
			{"name":"jane","address": "Park Lane 38"},
			{"name":"julie","address": "Park Lane 38"},
			{"name":"jack","address": "Apple st 52"}
		 ]

#Inserting data
mycollection.insert_many(myList)

#Data in database
print("Original data")
for i in mycollection.find():
	print(i)

#Delete one
mycollection.delete_one({"address":"Park Lane 38"})
#Deletes First Document whose address= park lane 38
for i in mycollection.find():
	print(i)

#Delete Many
mycollection.delete_many({"address":"Park Lane 38"})
#Deletes all Documents whose address= park lane 38
for i in mycollection.find():
	print(i)


mycollection.delete_many({})
#Deletes all Documents
for i in mycollection.find():
	print(i)
