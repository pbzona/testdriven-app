from json import load
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_restful import Resource, Api

load_dotenv()

# instantiate the app
app = Flask(__name__)
app.config.from_object('project.config.DevelopmentConfig')
api = Api(app)

class UsersPing(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'pong!'
    }

api.add_resource(UsersPing, '/users/ping')