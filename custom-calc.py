# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the descirption. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!

# Prompt the user to enter height
height = input("Enter height: ")

# Prompt the user to enter width
width = input("Enter width: ")

# Prompt the user to enter length
length = input("Enter length: ")

# Convert the input to an integer
height_of_cube_in_inches = int(height) * 3.9
width_of_cube_in_inches = int(width) * 5
length_of_cube_in_inches = int(length) * 3.9

# Print the length of the snowboard in inches
print("The area of the cube is:", height_of_cube_in_inches + width_of_cube_in_inches + length_of_cube_in_inches)
print(f"Its calculations are as flollows: height of {height}, width of {width}, and a length of {length}")


