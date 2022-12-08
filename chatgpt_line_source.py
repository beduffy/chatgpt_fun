import inspect

# Define a function that prints the line number of each line within itself
def print_line_numbers():
  # Get the current function's source code
  src = inspect.getsource(print_line_numbers)

  # Split the source code into individual lines
  lines = src.split('\n')

  # Print each line with its line number
  for i, line in enumerate(lines):
    print(i + 1, line)

# Call the print_line_numbers function to print the line numbers
print_line_numbers()# Define a function that prints the line number of each line within itself
def print_line_numbers():
  # Get the current function's source code
  src = inspect.getsource(print_line_numbers)

  # Split the source code into individual lines
  lines = src.split('\n')

  # Print each line with its line number
  for i, line in enumerate(lines):
    print(i + 1, line)

# Call the print_line_numbers function to print the line numbers
print_line_numbers()
