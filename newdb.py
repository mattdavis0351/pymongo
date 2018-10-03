# import the pymongo library
from pymongo import MongoClient

# create a new database
newclient = MongoClient('localhost', 27017)
newdb = newclient["pythondb"]
#create new colleciton
pycol = newdb["pycol"]
