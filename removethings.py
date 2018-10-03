# import the pymongo library
from pymongo import MongoClient

# create connection to a mongo client using host and port as arguments
client = MongoClient('localhost', 27017)
# connect to a database located on the client
employees = client["employees"]
# connect to a collection in a database
emps = employees['emps']

# create a query variable
query1 = {"fname":"brent"}

# delete a document based on the query created above.
emps.delete_one(query1)

# delete documents based on more complex parameters
# query2 = {"fname":{"$regex":"^j"}}
# x = emps.delete_many(query2)
#
# print(x.deleted_count, "documents deleted")
