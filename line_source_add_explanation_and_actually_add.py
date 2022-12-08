# Prompt: how would we change this code so that it change the file for the next runtime?

import inspect

# Define a function that adds new lines to the code on each running of the code
def add_lines():
  # Get the current function's source code
  src = inspect.getsource(add_lines)
  print('hey')

  # Split the source code into individual lines
  lines = src.split('\n')

  # Add a new line to the end of the source code
  new_line = 'print("This is a new line added on running the code.")'
  lines.insert(-1, new_line)

  # does not work

  # Join the lines into a single string
  new_src = '\n'.join(lines)

  # Execute the modified source code
  exec(new_src)

# Call the add_lines function to add new lines to the code
# add_lines()

# Open the file containing the code to be modified
with open('line_source_add_explanation_and_actually_add.py', 'r') as f:
  # Read the contents of the file
  src = f.read()

# Split the source code into individual lines
lines = src.split('\n')

# Add a new line to the end of the source code
new_line = 'print("This is a new line added on running the code.")'
lines.insert(-1, new_line)

# Join the lines into a single string
new_src = '\n'.join(lines)

# Open the file for writing
with open('line_source_add_explanation_and_actually_add.py', 'w') as f:
  # Write the modified code to the file
  f.write(new_src)

# Import the modified code from the file
from code_to_modify import *

# Call the add_lines function to add new lines to the code
print("This is a new line added on running the code.")
print("This is a new line added on running the code.")
print("This is a new line added on running the code.")
print("This is a new line added on running the code.")
print("This is a new line added on running the code.")
print("This is a new line added on running the code.")
print("This is a new line added on running the code.")
print("This is a new line added on running the code.")
print("This is a new line added on running the code.")
print("This is a new line added on running the code.")
print("This is a new line added on running the code.")
add_lines()