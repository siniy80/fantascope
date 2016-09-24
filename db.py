from pymongo import MongoClient

client = MongoClient()
db = client.fantascope

def getToken():
  return db.token.find_one().get("token")
