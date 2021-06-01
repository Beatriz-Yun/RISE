from flask import Flask
from flask_restful import Resource, Api, reqparse
from werkzeug.datastructures import FileStorage
from predict_food2 import predict
import tempfile

app = Flask(__name__)
app.logger.setLevel('INFO')

api = Api(app)

class Image(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('image',
                            type=FileStorage,
                            location='files',
                            required=True,
                            action='append',
                            help='provide a file')
        args = parser.parse_args()
        the_file = args['image']
        # save a temporary copy of the file
        ofile, ofname = tempfile.mkstemp()
        the_file.save(ofname)
        # predict
        result = predict(ofname)[0]

        # formatting the results as a JSON-serializable structure:
        output = {'result': [result]}

        return output

api.add_resource(Image, '/image/<string:fname>')

if __name__ == '__main__':
    app.run(debug=True)