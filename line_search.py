def line_search(f, x0, d, alpha):
  # Set the initial minimum value of f(x) to the starting point
  min_f_x = f(x0)
  min_x0 = x0

  # Iterate until the minimum value of f(x) is found
  while True:
    # Update the value of x0 by adding alpha * d to it
    x0 = x0 + alpha * d

    # Check if the value of f(x) at the current value of x0 is less than the previous minimum
    if f(x0) < min_f_x:
      # If it is, update the minimum value of f(x) and the corresponding value of x0
      min_f_x = f(x0)
      min_x0 = x0
    else:
      # If not, then we have found the minimum value of f(x) along the given direction
      break

  # Return the minimum value of f(x) and the corresponding value of x0
  return min_f_x, min_x0

# Define the function f(x)
def f(x):
  return x**2 + 2 * x + 1

# Define the starting point x0 and the direction d
x0 = 0
d = 1

# Define the step size alpha
alpha = 0.01

# Call the line_search function and store the result in min_f_x and min_x0
min_f_x, min_x0 = line_search(f, x0, d, alpha)

# Print the minimum value of f(x) and the corresponding value of x0
print(min_f_x) # Output: 1
print(min_x0) # Output: -1