from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
    "name": "James",
    "age": 20,
    "occupation": "software engineer"

    },
    {
    "name": "Max",
    "age": 20,
    "occupation": "retail assistant"

    },
    {
    "name": "Felix",
    "age": 20,
    "occupation": "Model"
    }

]

class User(Resource):

    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "user not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name),400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, name):


    def delete(self, name):
