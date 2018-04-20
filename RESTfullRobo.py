from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Status(Resource):
    def get(self):
        return {'hello': 'world'}


class Command(Resource):
    def post(self, command):
        print(request.json)
        return {'command': str(command)}


api.add_resource(Status, '/status')
api.add_resource(Command, '/command/<string:command>')
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
