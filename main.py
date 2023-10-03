import string
import secrets
import tkinter as tk

max_length = 16

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(characters) for i in range(max_length))

print(password)
