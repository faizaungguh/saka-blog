import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv() # panggil os dan dotenv untuk membaca .env, dan memanggil environment yang kita tentukan

# memuat environment
mongoHost = os.environ.get("mongodbHOST")
mongoURL = os.environ.get("mongodbURL")
mongoDBName = os.environ.get("mongodbName")

client = MongoClient(mongoURL, serverSelectionTimeoutMS=500)

dbName = mongoDBName
db = client[dbName] # nama db