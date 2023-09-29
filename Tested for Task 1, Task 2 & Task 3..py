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





# In[25]:


#Task 2: Working with databases
    
import sqlite3

conn = sqlite3.connect('users.db')

cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER
    )
''')

def add_user(name, email, age):
    cur.execute('INSERT INTO Users (name, email, age) VALUES (?, ?, ?)', (name, email, age))
    conn.commit()

def get_all_users():
    cur.execute('SELECT * FROM Users')
    return cur.fetchall()

def update_user(id, name, email, age):
    cur.execute('UPDATE Users SET name=?, email=?, age=? WHERE id=?', (name, email, age, id))
    conn.commit()

def delete_user(id):
    cur.execute('DELETE FROM Users WHERE id=?', (id,))
    conn.commit()

add_user('John Doe', 'john.doe@example.com', 30)
add_user('Jane Smith', 'jane.smith@example.com', 25)

print("All Users:")
print(get_all_users())

update_user(1, 'John Updated', 'john.doe.updated@example.com', 31)

print("All Users after update:")
print(get_all_users())

delete_user(2)

print("All Users after deletion:")
print(get_all_users())

conn.close()


# Explanation:

# Database Connection:
# The script establishes a connection to the SQLite database (or creates it if it doesn't exist) named "users.db".

# Table Creation:
# A "Users" table is created if it doesn't already exist, with columns for ID, name, email, and age.

# CRUD Operations:
# Create (Add User): add_user function inserts a new user into the Users table.
# Read (Get All Users): get_all_users function retrieves all users from the Users table.
# Update (Update User): update_user function modifies user data based on the user's ID.
# Delete (Delete User): delete_user function removes a user from the Users table based on the user's ID.

# Example Usage:
# Two users are added, then the first user's data is updated, and the second user is deleted.
# The state of the Users table is printed after each operation to demonstrate the CRUD operations.

# This structure allows for basic user data management with the ability to add, retrieve, update, and delete user records. SQLite is used here due to its simplicity and suitability for small-scale applications. For larger-scale applications or when there's a need for complex queries, other databases like PostgreSQL or MySQL might be more appropriate.


# In[ ]:


#Task 3: Integration with a Google API
    
import requests

def get_lat_long(api_key, address):
    
    endpoint = "https://maps.googleapis.com/maps/api/geocode/json"
  
    params = {
        'address': address,
        'key': api_key  
    }

    response = requests.get(endpoint, params=params)
    data = response.json() 
    
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        print(f'Latitude: {latitude}')
        print(f'Longitude: {longitude}')
        return latitude, longitude
    else:
        error_message = data.get('error_message', 'Unknown error occurred')
        print(f'Error: {error_message}')
        return None, None

    
   
    

api_key = 'YOUR_GOOGLE_MAPS_API_KEY'
address = '999 E Caribbean Dr, Sunnyvale, CA 94089, United States'

latitude, longitude = get_lat_long(api_key, address)

if latitude and longitude:
    print(f'Latitude: {latitude}')
    print(f'Longitude: {longitude}')
else:
    print('Failed to retrieve location data.')
    
    

# Explanation:

# Function get_lat_long:
# Accepts a Google API key and an address as parameters.
# Constructs the API endpoint with the provided address and API key.
# Sends a GET request to the Google Maps Geocoding API.
# Parses the JSON response and extracts the latitude and longitude if the status is 'OK'.

# Example Usage:
# Replace 'YOUR_GOOGLE_MAPS_API_KEY' with your actual Google Maps API key.
# The address '1600 Amphitheatre Parkway, Mountain View, CA' is used as an example.
# If the API request is successful (status is 'OK'), it prints the latitude and longitude. Otherwise, it prints an error message.

# Data Processing Approach:
# The script processes data in JSON format received from the API.
# It checks the status in the response to ensure that the request was successful (status is 'OK').
# If successful, it extracts latitude and longitude from the JSON response.

# This approach provides a clear separation of concerns, making the code easy to read and maintain. It utilizes the requests library for making HTTP requests and follows best practices for error handling to ensure that the script behaves gracefully even in case of API request failures.

