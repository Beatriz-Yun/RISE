from tensorflow import keras
#from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import *
import cv2

import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

def predict(fname):
    # img = image.load_img(fname, target_size=input_shape[:2])
    # img = image.img_to_array(img)

    img = cv2.imread(fname)
    img = cv2.resize(img, (224, 224))

    import numpy as np
    img = np.reshape(img, [1, 224, 224, 3])

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

    import pprint
    import sys

    file_name = 'test_image3.jpg'
    results = predict(file_name)
    pprint.pprint(results)