# import the pymongo library
from pymongo import MongoClient


# create a new database
newclient = MongoClient('localhost', 27017)
newdb = newclient["pythondb"]
# create new colleciton
heroes = newdb["heroes"]

# insert only one record
hulk = {"fname":"bruce", "lname":"banner", "alias":"hulk", "interests":[
"smashing", "anger", "new clothes"]}

heroes.insert_one(hulk)
