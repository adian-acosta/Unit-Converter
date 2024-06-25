import tkinter as tk
from unit_converter import convert_units

def converter():
    try:
        input_value = float(input_entry.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()
        result = convert_units(input_value, from_unit, to_unit)
        result_label.config(text=f"{result} {to_unit}")
    except ValueError as e:
        result_label.config(text=str(e))

# Create the main window
root = tk.Tk()
root.geometry("200x200")
root.title("Unit Converter")

# Creating the widgets
input_label = tk.Label(root, text="Value:")
input_entry = tk.Entry(root)
from_label = tk.Label(root, text="From:")
units = [
    "Miles",
    "Kilometers",
    "Pounds",
    "Kilograms",
    "Inches",
    "Centimeters"
]

from_unit_var = tk.StringVar()
from_unit_var.set(units[0])
from_dropdown_button = tk.OptionMenu(root, from_unit_var, *units)

to_label = tk.Label(root, text="To:")
to_unit_var = tk.StringVar()
to_unit_var.set(units[0])
to_dropdown_button = tk.OptionMenu(root, to_unit_var, *units)

convert_button = tk.Button(root, text="Convert", command=converter)
result_label = tk.Label(root, text="")

# Placing all the widgets
input_label.grid(row=0, column=0)
input_entry.grid(row=0, column=1, padx=10, pady=5)
from_label.grid(row=1, column=0, pady=5)
from_dropdown_button.grid(row=1, column=1, padx=10, pady=5)
to_label.grid(row=2, column=0, pady=5)
to_dropdown_button.grid(row=2, column=1, padx=10, pady=5)
convert_button.grid(row=3, column=1, pady=15)
result_label.grid(row=4, column=1, pady=5)

# Execute tkinter
root.mainloop()