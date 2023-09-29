#!/usr/bin/env python
# coding: utf-8

# In[24]:


#Task 1: Creating a neural network

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

train_labels = to_categorical(train_labels, 10)
test_labels = to_categorical(test_labels, 10)

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.2)

test_loss, test_accuracy = model.evaluate(test_images, test_labels)

print(f'Test Accuracy: {test_accuracy * 100:.2f}%')
print(f'Test Loss: {test_loss:.4f}')


# Explanation:

# Loading and Preprocessing Data:
# MNIST dataset is loaded and divided into training and testing sets.
# The pixel values (0 to 255) are normalized to the range of 0 to 1 by dividing by 255 to help the training process.

# Neural Network Architecture:
# Convolutional Layer: 32 filters of size (3, 3) with ReLU activation function. This layer is responsible for learning spatial hierarchies of features.
# MaxPooling Layer: Pooling layer with pool size (2, 2) to reduce the spatial dimensions.
# Flattening Layer: Flattens the 2D arrays to 1D array before passing to the dense layers.
# Dense Layers: Two dense layers with 64 and 10 neurons respectively. ReLU activation function is used in the first dense layer for introducing non-linearity, and softmax activation in the output layer for multi-class classification.

# Compilation:
# Optimizer: 'adam' optimizer is chosen for its adaptive learning rate properties.
# Loss Function: 'categorical_crossentropy' is used since this is a multi-class classification problem.
# Metrics: Accuracy is chosen as the metric to evaluate the model's performance.

# Training:
# The model is trained for 5 epochs with a batch size of 64.
# 20% of the training data is used as validation data to monitor the model's performance during training.

# Evaluation:
# The trained model is evaluated on the test dataset, and accuracy and loss metrics are printed.


# This configuration provides a good balance between complexity and accuracy for the MNIST dataset. The choice of the number of filters, filter size, and dense layer neurons are common starting points and can be adjusted for further experimentation. The model achieves reasonable accuracy within a short training time.


# In[ ]:




