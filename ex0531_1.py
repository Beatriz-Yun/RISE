from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import werkzeug

app = Flask(__name__)
api = Api(app)

class Upload(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parser.parse_args()

        file_object = args['file']

api.add_resource(Upload, '/upload')

if __name__ == '__main__':
    app.run(debug=True)