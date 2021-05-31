from flask import Flask, render_template, request
import json

app = Flask(__name__)

PATH = ""

ALLOWED_FORM = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_FORM

@app.route("/")
def showPage():
    return render_template('index.html')

@app.route("/loadData", methods=["GET", "POST"])
def loadData():

    result = [1,2,3,4,5]

    return json.dumps(result)

@app.route("/upload", methods=["POST"])
def upload():
    if request.method == 'POST':
        print("POST!")

        file = request.files['uploadedfile']
        path = PATH + file.filename;

        if file and allowed_file(file.filename):
            file.save(path)
            return "ok"

    return "upload Test"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5008)
