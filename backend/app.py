from flask import Flask
from connection import checkDatabase, dbName

app = Flask(__name__)

if __name__ == '__main__':
    from controllers import *
    app.run(debug=True)