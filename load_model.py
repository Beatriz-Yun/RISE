from flask import Flask, render_template, request
import numpy as np

from tensorflow import keras
from tensorflow.keras.optimizers import *
import cv2

app = Flask(__name__)

@app.route('/upload')
def basic():
    #image = str(request.form['test'])
    return render_template("upload.html")

@app.route('/predict', methods=['POST'])
def predict():
    value = request.form['file']

    f = request.files['file']
    Path = "./"
    f.save(Path+f.filename)
    model = keras.models.load_model(Path + "my_model_2.h5")
    optimizer = Adam(lr=0.00001)
    model.compile(loss='categorical_crossentropy',
                  optimizer=optimizer,
                  metrics=['accuracy'])

    test_data = Path + ".jpg"
    class_names = ['Chinese', 'Japanese', 'Korean']

    img = cv2.imread(Path + 'test_image4.jpg')
    img = cv2.resize(img, (224, 224))
    img = np.reshape(img, [1, 224, 224, 3])

    classes = np.argmax(model.predict(img), axis=-1)
    print(classes)
    names = [class_names[i] for i in classes]
    print(names)

# def post():
#     value = request.form['input']
#     return render_template('default.html', name=value)

if __name__ == '__main__':
    app.run(debug=True)