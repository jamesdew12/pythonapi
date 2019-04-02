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
