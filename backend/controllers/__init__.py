from flask import jsonify
from utils.error import handle404
from app import app

@app.route('/api')
def index():
    return jsonify(message="Hi, dunia!")

# error handler
app.register_error_handler(404, handle404)