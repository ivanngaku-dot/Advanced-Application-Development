# Program Name: Assignment3.py
# Course: IT3883/Section 3
# Student Name: Ivan Yann NGAKU FOSSO
# Assignment Number: Lab 3
# Due Date: 06/26/2026
# Purpose:This program converts Miles per Gallon (MPG) to Kilometers per Liter (KM/L).
# The result updates automatically as the user types, the program also handles blank input or letters without crashing.
# Resources:Notes used in class and powerpoint documents.
# Python Tkinter documentation

import tkinter as tk

# Function to convert MPG to KM/L
def convert(event=None):
    try:
        # Read the value from the entry box
        mpg = float(entry_mpg.get())

        # Convert MPG to KM/L
        km_l = mpg * 0.425143707

        # Display the result with 2 decimal places
        result_label.config(text=f"{km_l:.2f} KM/L")

    except ValueError:
        # If the user types letters or leaves the box blank
        result_label.config(text="0.00 KM/L")


# Create the main window
window = tk.Tk()
window.title("MPG to KM/L Converter")
window.geometry("300x180")

# Label for MPG input
label1 = tk.Label(window, text="Enter MPG:")
label1.pack(pady=5)

# Entry box
entry_mpg = tk.Entry(window)
entry_mpg.pack()

# Update the result whenever a key is released
entry_mpg.bind("<KeyRelease>", convert)

# Label for the result
label2 = tk.Label(window, text="Kilometers Per Liter:")
label2.pack(pady=10)

# Result display
result_label = tk.Label(window, text="0.00 KM/L", font=("Arial", 12))
result_label.pack()

# Keep the window open
window.mainloop()