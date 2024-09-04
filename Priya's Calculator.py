import tkinter as tk
import math  # Import the math module for trigonometric functions

# Function to handle button clicks and update the display with the clicked value
def button_click(item):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(item))

# Function to clear the entire display
def button_clear():
    entry.delete(0, tk.END)

# Function to remove the last character from the display
def button_back():
    current_text = entry.get()
    if len(current_text) > 0:
        entry.delete(len(current_text) - 1, tk.END)

# Function to evaluate the expression and display the result
def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to calculate square root or cube root
def button_sqrt_cube(is_cube=False):
    try:
        current_text = entry.get()
        number = float(current_text)
        if is_cube:
            result = round(number ** (1/3), 8)  # Calculate cube root
        else:
            result = round(math.sqrt(number), 8)  # Calculate square root
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to calculate trigonometric functions
def button_trig(func):
    try:
        current_text = entry.get()
        angle = math.radians(float(current_text))  # Convert to radians
        if func == 'sin':
            result = round(math.sin(angle), 8)
        elif func == 'cos':
            result = round(math.cos(angle), 8)
        elif func == 'tan':
            result = round(math.tan(angle), 8)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Initialize the main window
root = tk.Tk()
root.title("Calculator by Priya")

# Entry widget to display the expression and result
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4)

# Button layout including square root, cube root, and trigonometric functions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('√', 5, 0), ('√³', 5, 1), ('sin(θ)', 5, 2), ('cos(θ)', 5, 3),
    ('tan(θ)', 6, 0)
]

# Button colors
button_colors = {
    'numbers': {'bg': '#F0F0F0', 'fg': '#000000'},  # Light gray background for numbers
    'operators': {'bg': '#FFD580', 'fg': '#000000'},  # Light orange background for operators
    'functions': {'bg': '#ADD8E6', 'fg': '#000000'},  # Light blue background for trigonometric and root functions
    'equal': {'bg': '#90EE90', 'fg': '#000000'},  # Light green background for equal sign
    'clear': {'bg': '#FF3B30', 'fg': '#000000'},  # Light pink background for clear button
    'back': {'bg': '#FFD580', 'fg': '#000000'},  # Light orange background for back button
    'maroon2': {'bg': '#F4A7B9', 'fg': '#000000'},  # Lighter maroon (pinkish) background
}

# Create and place the buttons on the grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=10, height=2, command=button_equal, **button_colors['equal'])
    elif text in ['+', '-', '*', '/']:
        button = tk.Button(root, text=text, width=10, height=2, command=lambda t=text: button_click(t), **button_colors['operators'])
    elif text in ['√', '√³', 'sin(θ)', 'cos(θ)', 'tan(θ)']:
        if text == '√':
            button = tk.Button(root, text=text, width=10, height=2, command=lambda: button_sqrt_cube(is_cube=False), **button_colors['functions'])
        elif text == '√³':
            button = tk.Button(root, text=text, width=10, height=2, command=lambda: button_sqrt_cube(is_cube=True), **button_colors['functions'])
        else:
            button = tk.Button(root, text=text, width=10, height=2, command=lambda t=text: button_trig(t[:3]), **button_colors['functions'])
    else:
        button = tk.Button(root, text=text, width=10, height=2, command=lambda t=text: button_click(t), **button_colors['numbers'])
    button.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(root, text='C', width=5, height=2, command=button_clear, **button_colors['clear'])
clear_button.grid(row=6, column=1, sticky="nsew")

# Back button
back_button = tk.Button(root, text='←', width=5, height=2, command=button_back, **button_colors['back'])
back_button.grid(row=6, column=2, columnspan=2, sticky="nsew")

# Start the main loop to keep the application running
root.mainloop()