from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import *
import tensorflow.keras.applications.resnet50 as resnet50
import cv2

import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'



def predict(fname):
    # img = image.load_img(fname, target_size=input_shape[:2])
    # img = image.img_to_array(img)

    # img = cv2.imread(fname)
    # img = cv2.resize(img, (224, 224))
    # img = np.reshape(img, [1, 224, 224, 3])

    img = image.load_img(fname, target_size=(224, 224))
    x = image.img_to_array(img)

    import numpy as np
    img = np.expand_dims(x, axis=0)
    # img = np.vstack([img])

    img = resnet50.preprocess_input(img)
    print(np.shape(img))

    model = keras.models.load_model("my_model_2.h5")
    optimizer = Adam(lr=0.00001)
    model.compile(loss='categorical_crossentropy',
                  optimizer=optimizer,
                  metrics=['accuracy'])

    class_names = ['Chinese', 'Japanese', 'Korean']

    classes = np.argmax(model.predict(img), axis=-1)
    print(classes)
    result = [class_names[i] for i in classes]
    print(result)

    return result[0]

if __name__ == '__main__':
    file_name = 'test_image3.jpg'
    results = predict(file_name)
    print(results)