import pymongo
from pymongo.errors import BulkWriteError

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
# Database gabakal ada kalo di print, selama belom ada collections dan isinya
#print(myclient.list_database_names())
mycol = mydb["customers"]
# Database gabakal ada kalo di print, selama belom ada collections dan isinya
#print(myclient.list_database_names())
mydict = {"name": "John1", "address": "Highway 37" }
x = mycol.insert_one(mydict)

mydict = {"name": "John21", "address": "Highway 3711", "tes" : "a" }
x = mycol.insert_one(mydict)

mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

try:
    x = mycol.insert_many(mylist)
except BulkWriteError as bwe:
    #print(bwe.details)
    print(bwe.details['writeErrors'][0]['errmsg'])

# Sekarang udah ada
print(myclient.list_database_names())

print(mycol.find_one())
for i in mycol.find({ "address": "Highway 37" }):
    print(i)

mydoc = mycol.find().sort("name", 1)
#mydoc = mycol.find().sort("name", -1) # Descending
for x in mydoc:
  print(x)

myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery)

myquery = { "address": "Highway 37" }
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }
mycol.update_one(myquery, newvalues)

# DELETE ALL ENTRY, TRUNCATE
# x = mycol.delete_many({})
# print(x.deleted_count, " documents deleted.")

# DROP TABLE
# mycol.drop()