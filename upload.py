from flask import Flask, render_template, request
from predict_food2 import predict_food

app = Flask(__name__)

@app.route('/upload')
def basic():
    return render_template("upload.html")

@app.route('/predict', methods=['POST'])
def predict():
    f = request.files['file']
    # Path = "./"
    # f.save(Path+f.filename)
    result = predict_food(f.filename)

    # formatting the results as a JSON-serializable structure:
    output = {'result': [result]}

    return output

# def post():
#     value = request.form['input']
#     return render_template('default.html', name=value)

if __name__ == '__main__':
    app.run(debug=True)