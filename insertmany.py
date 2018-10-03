# import the pymongo library
from pymongo import MongoClient


# create a new database
newclient = MongoClient('localhost', 27017)
newdb = newclient["pythondb"]
# create new colleciton
heroes = newdb["heroes"]

# insert only one record
goodguys = [
{"fname":"clark", "lname":"kent", "alias":"superman", "interests":[
"phone booths", "flying", "leaping"]}
{"fname":"peter", "lname":"parker", "alias":"spiderman", "interests":[
"pictures", "webs", "science"]}
{"fname":"steve", "lname":"rogers", "alias":"captian america", "interests":[
"freedom", "taxes", "service"]}
{"fname":"tony", "lname":"stark", "alias":"iron man", "interests":[
"metal", "money", "microcomputers"]}
{"fname":"clint", "lname":"barton", "alias":"hawkeye", "interests":[
"archery", "birds", "flying"]}
{"fname":"matt", "lname":"davis", "alias":"fat turtle", "interests":[
"shells", "strawberries", "pizza"]}
{"fname":"wanda", "lname":"maximoff", "alias":"scarlet witch", "interests":[
"fire", "halloween", "the force"]}
{"fname":"natasha", "lname":"romanoff", "alias":"black widow", "interests":[
"nighttime", "spiders", "webs"]}
{"fname":"diana", "lname":, "alias":"wonder woman", "interests":[
"wonderful", "gold", "justice"]}
]

heroes.insert_many(goodguys)
