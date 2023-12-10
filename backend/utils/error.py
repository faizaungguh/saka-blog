from flask import jsonify, make_response

def handle404(error):
        return make_response(jsonify(
                        {
                        "errorCode": error.code, 
                        "errorDescription": "Endpoint tidak ditemukan",
                        "errorDetailedDescription": error.description,
                        "errorName": error.name
                        }), 404)
