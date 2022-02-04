import os, random
import tensorflow as tf
import numpy as np



path = "./test-images-resize"
dir_to_model = "./save-models/model_0/Dog-cat-recognition.h5"

model = tf.keras.models.load_model(dir_to_model)
# model.summary()

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

images_dir = os.listdir(path)
images = []
for i in images_dir:
    i = path + "/" + i
    images.append(mpimg.imread(i))

images = np.array(images).reshape(-1, 150, 150, 3)
prediction = model.predict(images)

for i in range(len(images_dir)):
    print(images_dir[i] + " is " + " cats" if (prediction[i] < 0.1) else images_dir[i] + " is " + " dogs", end = " - ")
    print(prediction[i])