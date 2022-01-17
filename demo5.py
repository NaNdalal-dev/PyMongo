import pymongo

client = pymongo.MongoClient("localhost",27017)

mydb = client["MyDataBase"]

#Creating Customers Collection 
mycollection = mydb["Customers"]

myList = [
			{"_id":"1","name":"john","address": "Park Lane 38"},
			{"_id":"2","name":"jane","address": "Park Lane 38"},
			{"_id":"3","name":"julie","address": "Park Lane 38"},
		 ]

#Inserting data
mycollection.insert_many(myList)

for i in mycollection.find():
	print(i)

#Update One
old_value = {"address":"Park Lane 38"}
new_value = { "$set":{"address":"Dallas"} }

mycollection.update_one(old_value,new_value)

for i in mycollection.find():
	print(i)

#Update many
old_value = {"address":"Park Lane 38"}
new_value = { "$set":{"address":"Dallas"} }

mycollection.update_many(old_value,new_value)

for i in mycollection.find():
	print(i)