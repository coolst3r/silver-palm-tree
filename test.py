import string
import random
import tkinter as tk

# Define the maximum length
max_length = 2000

# Initialize an empty string
random_string = ""

# Generate random letters until the length reaches max_length
while len(random_string) < max_length:
    random_letter = random.choice(string.ascii_letters)
    random_string += random_letter


print(random_string)