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
add_lines()