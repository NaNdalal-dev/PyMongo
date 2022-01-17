import pymongo

client = pymongo.MongoClient("localhost",27017)

mydb = client["MyDataBase"]

#Creating Customers database 
mycollection = mydb["CustomersData71"]

myList = [
			{"name":"john","address": "Park Lane 38"},
			{"name":"jane","address": "Park Lane 38"},
		 ]

#To Delete the collection use drop method
mycollection.drop()

