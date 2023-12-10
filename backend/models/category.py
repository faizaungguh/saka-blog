from flask_pymongo import pymongo
from datetime import datetime
from marshmallow import Schema, fields, validate
import pytz

mongo = pymongo()

class Category:
    # menentukan field nya
    def __init__(self, category):
        self.category = category
        self.slug = self.generateSlug()
        self.created_at = self.generateTime()

    # generate slug - Wira Kartika ->
    def generateSlug(self):
        return self.category.lower().replace(" ", "-")
    
    # ubah timezone ke Indonesia
    def generateTime(self):
        zona = pytz.timezone('Asia/Jakarta')
        return datetime.now(zona)

    # menyimpan kategori
    def save(self):
        mongo.db.category.insert_one({
            'category': self.category,
            'slug': self.slug,
            'created_at': self.created_at
        })

    # endpoint /
    @staticmethod
    def getAll():
        return mongo.db.category.find()