from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    from controllers import *
    app.run(debug=True)