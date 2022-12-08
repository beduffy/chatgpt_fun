# do it without sklearn

# Import the necessary modules
import numpy as np

# Load the data set
data = np.loadtxt('data.csv', delimiter=',')

# Split the data set into a training set and a testing set
train_data = data[:500, :-1]
train_labels = data[:500, -1]
test_data = data[500:, :-1]
test_labels = data[500:, -1]

# Define a sigmoid function
def sigmoid(x):
  return 1 / (1 + np.exp(-x))

# Define the logistic regression model
def logistic_regression(x, w):
  return sigmoid(np.dot(x, w))

# Define the loss function
def loss(x, y, w):
  y_pred = logistic_regression(x, w)
  return -np.mean(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))

# Define the gradient descent algorithm
def gradient_descent(x, y, w, learning_rate, n_iterations):
  # Perform the specified number of iterations
  for i in range(n_iterations):
    # Calculate the gradient of the loss function
    grad = np.dot(x.T, (logistic_regression(x, w) - y)) / len(x)

    # Update the weights using the gradient and the learning rate
    w -= learning_rate * grad
  
  # Return the updated weights
  return w

# Define a function to evaluate the performance of the logistic regression model
def evaluate(x, y, w):
  # Make predictions using the logistic regression model
  y_pred = logistic_regression(x, w)

  # Round the predictions to the nearest integer
  y_pred = np.round(y_pred)

  # Calculate the accuracy, precision, and recall
  accuracy = np.mean(y_pred == y)
  precision = np.mean(y_pred[y == 1] == 1)
  recall = np.mean(y_pred[y == 1] == y[y == 1])

  # Return the performance metrics
  return accuracy, precision, recall

# Initialize the weights with random values
np.random.seed(0)
w = np.random.random(train_data.shape[1])

# Set the learning rate and the number of iterations
learning_rate = 0.01
n_iterations = 1000

# Train the logistic regression model using gradient descent
w = gradient_descent(train_data, train_labels, w, learning_rate, n_iterations)

# Evaluate the performance of the logistic regression model
accuracy, precision, recall = evaluate(test_data, test_labels, w)

# Print the performance metrics
print('Accuracy:', accuracy)
print('Precision:', precision)
print('Recall:', recall)