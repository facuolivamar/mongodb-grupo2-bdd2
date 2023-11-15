import pymongo
from pymongo import MongoClient
MONGO_URI = "mongodb+srv://lolo:pepe1234@prueba1.hvgxgoh.mongodb.net/?retryWrites=true&w=majority"
myclient = pymongo.MongoClient(MONGO_URI)
mydb = myclient["pruebaaaa"]
mycol = mydb["preuebaa"]
'''''
client = MongoClient(MONGO_URI)
for db_name in client.list_database_names():
     print(db_name)
'''''
#                 ----------
#                 - CREATE -
#                 ----------
'''''
mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

# --------------------------------------------------------

mylist = [
  {"name": "John", "address": "Highway 37"},
  {"name": "Peter", "address": "Lowstreet 27"},
  {"name": "Amy", "address": "Apple st 652"},
  {"name": "Ben", "address": "Park Lane 38"},
]

x = mycol.insert_many(mylist)

print(x.inserted_ids)
'''''
#                  --------
#                  - READ -
#                  --------
'''''
myquery = { "address": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
'''''
#                 ----------
#                 - UPDATE -
#                 ----------
'''''
result = mycol.update_one({"name": "John"}, {"$set": {"address": "New Highway 1"}})

print(f"Se encontro {result.matched_count} documento y se modifico {result.modified_count} documento.")
'''''
#                 ----------
#                 - DELETE -
#                 ----------
'''''
mydb.mycol.delete_many(
  {"address": "Lowstreet 27"}
)
'''''