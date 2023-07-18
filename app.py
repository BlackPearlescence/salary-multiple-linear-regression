from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return make_response({"message" : "Hello, World!"},200)
    
api.add_resource(HelloWorld, "/")

if __name__ == "__main__":
    app.run(debug=True)