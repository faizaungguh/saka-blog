from flask import jsonify
from connection import checkDatabase, dbName
from app import app

@app.route('/')
def index():
    return jsonify(message="Hi, dunia!")