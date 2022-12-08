# Import the necessary modules
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load the data set
data = np.loadtxt('data.csv', delimiter=',')

# Split the data set into a training set and a testing set
train_data = data[:500, :-1]
train_labels = data[:500, -1]
test_data = data[500:, :-1]
test_labels = data[500:, -1]

# Create a logistic regression model
model = LogisticRegression()

# Fit the logistic regression model to the training set
model.fit(train_data, train_labels)

# Use the logistic regression model to make predictions on the testing set
predictions = model.predict(test_data)

# Evaluate