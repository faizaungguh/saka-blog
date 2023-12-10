from app import app
# from category import categoryBP
from utils.error import handle404

# endpoint /api/category
# app.register_blueprint(categoryBP, url_prefix='/api')
# error handler
app.register_error_handler(404, handle404)