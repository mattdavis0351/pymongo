# import the pymongo library
from pymongo import MongoClient

# create connection to a mongo client using host and port as arguments
client = MongoClient('localhost', 27017)
# connect to a database located on the client
employees = client["employees"]
# connect to a collection in a database
emps = employees['emps']

# create a query variable
query1 = {"fname":"john"}

# use that variable against a collection stored in a new variable to iterate over
empdoc = emps.find(query1)

for e in empdoc:
    print(e)

# a more complex query
query2 = {"salary":{"$gt":150000}}

emppay = emps.find(query2)

for e in emppay:
    print(e)

    
