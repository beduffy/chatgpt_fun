def calculate_mass_of_sun():
    return 1.9891e30

def calculate_mass_of_earth():
    return 5.972e24 

def sum_of_two_numbers(a, b):
    return a + b

publisher = rospy.Publisher('/copilot/steering', Float32, queue_size=10)