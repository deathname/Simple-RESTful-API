import flask
from flask import Flask
from flask_restful import Resource, Api, reqparse

users = [
    {
        "name": "Shakti",
        "age": 21
    },
    {
        "name": "Sanchit",
        "age": 22
    }
]


class User(Resource):

    def delete(self, name):
        for user in users:
            if user["name"] == name:
                del user
                return 200, "OK"

        return 400, "BAD"

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("age")

        args = parser.parse_args()

        for user in users:
            if user["name"] == name:
                return "User exists",400

        new_user = {
            "name": name,
            "age": args["age"]
        }
        users.append(new_user)
        return new_user,200

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("age")

        args = parser.parse_args()

        for user in users:
            if user["name"] == name:
                return "User exists",400

        new_user = {
            "name": name,
            "age": args["age"]
        }
        users.append(new_user)
        return new_user,200

    def get(self, name):
        resp = {}

        for user in users:
            if user["name"] == name:
                resp["name"] = user["name"]
                resp["age"] = user["age"]
                return "OK",200

        return "BAD",400


app = Flask(__name__)
api = Api(app)

api.add_resource(User,"/users/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)