import pymongo

client = pymongo.MongoClient("localhost",27017)

mydb = client["MyDataBase"]

mycollection = mydb["Student"]

#Find One
# print(mycollection.find_one())

# #Find all
# data = mycollection.find()
# for each_record in data:
# 	print(each_record)

#Return Only Some Fields
for each_record in mycollection.find({},{"address": 0}):
  print(each_record)
#Excluding address field

