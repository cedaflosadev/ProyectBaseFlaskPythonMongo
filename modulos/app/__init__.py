from flask import Flask
import json
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS, cross_origin
import datetime 

class JSONEncoder(json.JSONEncoder):

    def default(self,o):
        if isinstance(o,ObjectId):
            return str(o)
        if isinstance(o,datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self,o)

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config['MONGO_URI']='mongodb+srv://flask:Flask123@cluster0.lbsm5.mongodb.net/flasktutorial?retryWrites=true&w=majority'
app.json_encoder = JSONEncoder
mongo = PyMongo(app)

from app.controladores import usuarios

