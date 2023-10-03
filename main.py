import string
import random
import tkinter as tk

# Define the maximum length
max_length = 2000

# Initialize an empty string
random_string = ""

while len(random_string) < max_length:
    random_number = hrng_library.get_random_number()
    random_ascii_character = chr(random_number % 128)  # Ensure it's a valid ASCII character
    random_string += random_ascii_character

random_numbers = [random.randint(0, 255) for _ in range(1000)]
random_nummmy = ''.join(map(chr, random_numbers))

print(random_string+random_nummy)

