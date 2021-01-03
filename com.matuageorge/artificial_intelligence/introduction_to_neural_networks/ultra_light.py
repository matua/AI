# https://colab.research.google.com/drive/1otYe5RPzGc_3ZdMIw94vbC66ODi1yfSQ?usp=sharing

# Libraries loading
from tensorflow.keras.datasets import mnist
from tensorflow.keras import utils
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

(x_train_org, y_train_org), (x_test_org, y_test_org) = mnist.load_data()

# Normalization and transformation of x_train and y_train
x_train_org = x_train_org.reshape(60000, 784)
x_test_org = x_test_org.reshape(10000, 784)
x_train = x_train_org.astype('float32') / 255
x_test = x_test_org.astype('float32') / 255
y_train = utils.to_categorical(y_train_org, 10)
y_test = utils.to_categorical(y_test_org, 10)

# Neural network creation
model = Sequential()
model.add(Dense(800, input_dim=784, activation="relu"))
model.add(Dense(400, activation="relu"))
model.add(Dense(10, activation="softmax"))
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Neural network training
model.fit(x_train, y_train, batch_size=128, epochs=15, verbose=1)
