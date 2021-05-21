import keras

import tensorflow as tf
tf.test.is_gpu_available() # True/False

# Or only check for gpu's with cuda support
print(tf.test.is_gpu_available(cuda_only=True))

from keras.layers import Dense, Dropout, GlobalAveragePooling1D, Flatten
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv1D, MaxPool1D, BatchNormalization,Activation,MaxPooling1D
from keras.models import Model
from keras import applications
from keras.optimizers import SGD
#from load_data import load_resized_training_data, load_resized_validation_data
from sklearn.metrics import log_loss
import numpy as np
#from densenet121_models import densenet121_model 
from sklearn.metrics import roc_curve, auc, accuracy_score
from sklearn.metrics import classification_report,confusion_matrix
import matplotlib.pyplot as plt
num_classes=2
#model 1
model = Sequential()

model.add(Conv1D(32, kernel_size = 3, activation='relu', input_shape = (1,240)))
model.add(BatchNormalization())
model.add(Conv1D(32, kernel_size = 5, strides=2, padding='same', activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.4))

model.add(Conv1D(64, kernel_size = 3, activation='relu'))
model.add(BatchNormalization())
model.add(Conv1D(64, kernel_size = 5, strides=2, padding='same', activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.4))

model.add(Flatten())
#model.add(Dropout(0.4))
model.add(Dense(num_classes, activation='softmax',name='predictions'))

# use adam optimizer and categorical cross entropy cost
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])


model.summary()
