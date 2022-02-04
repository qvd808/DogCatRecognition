##Preprocess the image
# from bitarray import test
from keras.preprocessing.image import ImageDataGenerator

train_data_dir = "./sort-folder"
test_data_dir = "./cats_and_dogs_filtered/validation"



train_dataGen = ImageDataGenerator(rescale = 1.0/255)
test_dataGen = ImageDataGenerator(rescale = 1.0/255)

train_generator = train_dataGen.flow_from_directory(directory = train_data_dir,
                                                    target_size = (150, 150),
                                                    batch_size = 32,
                                                    class_mode = "binary")

test_generator = test_dataGen.flow_from_directory(directory=test_data_dir,
                                                    target_size=(150, 150),
                                                    batch_size=32,
                                                    class_mode="binary")


##Create a CNN model
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D

model = Sequential()
model.add(Conv2D(64, kernel_size = (5,5), activation = "relu", input_shape = (150, 150, 3)))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Conv2D(128, kernel_size = (5,5), activation = "relu"))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Conv2D(128, kernel_size = (5,5), activation = "relu"))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Flatten())
model.add(Dense(256, activation = "relu"))
model.add(Dense(1, activation = "sigmoid"))

sgd = tf.keras.optimizers.SGD(learning_rate=0.1)
model.compile(loss = "mean_squared_error", optimizer = sgd, metrics = ["accuracy"])
history = model.fit(train_generator, epochs = 10, verbose = 1, validation_data = (test_generator), steps_per_epoch = 25000/32, validation_steps = 1000/32)


############################## Save the model #########################################
import os, shutil
if (not os.path.exists("./save-models")):
    os.mkdir("./save-models")

size = len(next(os.walk('./save-models'))[1])
dir = "./save-models/model_" + str(size)
os.mkdir(dir)

model.save(dir + "/Dog-cat-recognition.h5")
from reportWriter import Writer
##Information on report
train_size = len(next(os.walk("./sort-folder/cats"))
                 [2]) + len(next(os.walk("./sort-folder/dogs"))[2])
test_size = len(next(os.walk("./cats_and_dogs_filtered/validation/cats"))
                [2]) + len(next(os.walk("./cats_and_dogs_filtered/validation/dogs"))[2])
batch_size = 32
target_size = (150, 150)
Writer(train_size, test_size, batch_size, target_size, dir)

## save the code for the model.py
shutil.copy(os.path.basename(__file__), dir)

######################################################################################

#Figure out the learning results
import matplotlib.pyplot as plt
loss = history.history["loss"]
val_loss = history.history["val_loss"]

learning_count = len(loss) + 1
plt.plot(range(1, learning_count), loss, marker = "+", label = "loss")
plt.plot(range(1, learning_count), val_loss, marker = ".", label = "val_loss")
plt.legend(loc = "best", fontsize = 10)
plt.xlabel("learning_count")
plt.ylabel("loss")
plt.savefig(dir + "/Loss-vs-val_loss.jpg", bbox_inches = "tight", dpi = 150)
plt.show()

accuracy = history.history["accuracy"]
val_accuracy = history.history["val_accuracy"]

learning_count = len(loss) + 1

plt.plot(range(1, learning_count), accuracy, marker = "+", label = "accuracy")
plt.plot(range(1, learning_count), val_accuracy, marker = ".", label = "val_accuracy")
plt.xlabel("learning_count")
plt.ylabel("accuracy")
plt.savefig(dir + "/Accuracy-vs-val_accuracy.jpg", bbox_inches = "tight", dpi = 150)
plt.show()
