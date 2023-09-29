# MLOpsTest

Task 1: Creating a Neural Network for MNIST Classification

Capabilities:
The code provides a simple neural network using TensorFlow for classifying images from the MNIST dataset.
Capable of training the network and evaluating its performance.
The network architecture includes convolutional layers, max-pooling, flattening, and dense layers for classification.

Installation:
Ensure you have Python installed on your system.
Install required libraries using pip: pip install tensorflow numpy

Usage:
Clone the GitHub repository: git clone https://github.com/rifatblack/MLOpsTest.git
Navigate to the project directory: cd MLOpsTest
Run the Python script: python Tested for Task 1.py
Important Details:

The code uses TensorFlow and the MNIST dataset.
The neural network architecture can be modified for experimentation.
Training parameters (epochs, batch size) can be adjusted in the script.

Task 2: Working with Databases

Capabilities:
The code creates an SQLite database and provides functions for adding, retrieving, updating, and deleting user data.
Demonstrates CRUD (Create, Read, Update, Delete) operations in SQLite.

Installation:
Ensure you have Python installed on your system.
No additional libraries are required as SQLite is part of the Python standard library.

Usage:
Clone the GitHub repository: git clone https://github.com/rifatblack/MLOpsTest.git
Navigate to the project directory: cd MLOpsTest
Run the Python script: python Tested for Task 2.py
Important Details:

The script establishes a connection to an SQLite database (users.db).
Users can be added, retrieved, updated, and deleted using the provided functions.


Task 3: Integration with a Google API
Capabilities:

The code uses the Google Maps Geocoding API to retrieve latitude and longitude based on an address.
Sends HTTP requests to the API and processes JSON responses.
Installation:

Ensure you have Python installed on your system.
Install the requests library using pip: pip install requests
Usage:

Clone the GitHub repository: git clone https://github.com/rifatblack/MLOpsTest.git
Navigate to the project directory: cd MLOpsTest
Replace 'YOUR_GOOGLE_MAPS_API_KEY' with an actual Google Maps API key in the google_api_integration.py file.
Run the Python script: python Tested for Task 3.py

Important Details
The script uses the requests library to interact with the Google Maps Geocoding API.
It processes JSON responses to extract latitude and longitude.
Ensure your API key has permissions for the Geocoding API.


Note:
Ensure proper error handling and security practices if deploying these scripts in production environments.
Follow the instructions in each README.md file for detailed usage guidelines.
Adhere to best software development practices and maintain clean, readable code.
