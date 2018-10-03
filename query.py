# import the pymongo library
from pymongo import MongoClient

# create connection to a mongo client using host and port as arguments
client = MongoClient('localhost', 27017)
# connect to a database located on the client
employees = client["employees"]
# connect to a collection in a database
emps = employees['emps']


# query the collection for a single docuemnt
single = emps.find_one()
print(single)

# query the colleciton for all documents:
for d in emps.find():
    print(d)

# query the collection for specific documents
for d in emps.find({"fname":"brent"}):
    print(d)
