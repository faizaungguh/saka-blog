import os
from flask import jsonify
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

def checkConnection(): # untuk cek ada tidaknya koneksi
    try:
        client.server_info()
        print("koneksi berhasil")
        return True
    except Exception as e:
        print(f"Gagal terkoneksi dengan MongoDB, pastikan koneksinya")
        return False

def checkDatabase(dbName): # untuk cek ada tidaknya db
    try:
        if dbName in client.list_database_names():
            print(f"Database {dbName} ditemukan.")
            return True
        else:
            print(f"Database {dbName} tidak ditemukan.")
            return False
    except Exception as e:
        print(f"Error checking database: {e}")
        return False

# Cek koneksi
checkConnection()
checkDatabase(dbName)