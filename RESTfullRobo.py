from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class Switch1(Resource):
    def post(self, state):
        print(request.json)
        return {'switch': str(state)}


api.add_resource(HelloWorld, '/')
api.add_resource(Switch1, '/switch<int:state>')
if __name__ == '__main__':
    app.run(debug=True)
