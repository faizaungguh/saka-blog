from flask import Blueprint, jsonify, request
from models import Category

categoryBP = Blueprint('category_bp', __name__)

@categoryBP.route('/category', methods=['GET'])
def getCategory():
    category = list(Category.get_all())
    return jsonify({'kategori': category})