from decimal import DivisionByZero
import tkinter as tk
from math import *

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    try:
        f_num = float(first_number)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
    else:
        entry.delete(0, tk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    
    if math == "addition":
        try:
            entry.insert(0, f_num + float(second_number))
        except ValueError:
            entry.insert(0, "Error")

    if math == "subtraction":
        try:
            entry.insert(0, f_num - float(second_number))
        except ValueError:
            entry.insert(0, "Error")

    if math == "multiplication":
        try:
            entry.insert(0, f_num * float(second_number))
        except ValueError:
            entry.insert(0, "Error")

    if math == "division":
        try:
            entry.insert(0, f_num / float(second_number))
        except ZeroDivisionError:
            entry.insert(0, "Error")

    if math == "power":
        try:
            entry.insert(0, f_num ** float(second_number))
        except ValueError:
            entry.insert(0, "Error")

    if math == "log":
        try:
            entry.insert(0, log10(f_num))
        except ValueError:
            entry.insert(0, "Error")

    if math == "exp":
        try:
            entry.insert(0, e ** f_num)
        except ValueError:
            entry.insert(0, "Error")

    if math == "sin":
        try:
            entry.insert(0, sin(radians(f_num)))
        except ValueError:
            entry.insert(0, "Error")

    if math == "cos":
        try:
            entry.insert(0, cos(radians(f_num)))
        except ValueError:
            entry.insert(0, "Error")

    if math == "tan":
        try:
            entry.insert(0, tan(radians(f_num)))
        except ValueError:
            entry.insert(0, "Error")

def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    try:
        f_num = float(first_number)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
    else:
        entry.delete(0, tk.END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    try:
        f_num = float(first_number)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
    else:
        entry.delete(0, tk.END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    try:
        f_num = float(first_number)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
    else:
        entry.delete(0, tk.END)

def button_power():
    first_number = entry.get()
    global f_num
    global math
    math = "power"
    try:
        f_num = float(first_number)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
    else:
        entry.delete(0, tk.END)

def button_log():
    first_number = entry.get()
    global f_num
    global math
    math = "log"
    try:
        f_num = float(first_number)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
    else:
        entry.delete(0, tk.END)

def button_exp():
    first_number = entry.get()
    global f_num
    global math
    math = "exp"
    try:
        f_num = float(first_number)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
    else:
        entry.delete(0, tk.END)

def button_sin():
    first_number = entry.get()
    global f_num
    global math
    math = "sin"
    try:
        f_num = float(first_number)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
    else:
        entry.delete(0, tk.END)

def button_cos():
    first_number = entry.get()
    global f_num
    global math
    math = "cos"
    try:
        f_num = float(first_number)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
    else:
        entry.delete(0, tk.END)

def button_tan():
    first_number = entry.get()
    global f_num
    global math
    math = "tan"
    try:
        f_num = float(first_number)
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
    else:
        entry.delete(0, tk.END)

# Define Buttons

button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = tk.Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = tk.Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=button_clear)

button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = tk.Button(root, text="/", padx=41, pady=20, command=button_divide)
button_power = tk.Button(root, text="^", padx=40, pady=20, command=button_power)
button_log = tk.Button(root, text="log", padx=34, pady=20, command=button_log)
button_exp = tk.Button(root, text="exp", padx=34, pady=20, command=button_exp)
button_sin = tk.Button(root, text="sin", padx=34, pady=20, command=button_sin)
button_cos = tk.Button(root, text="cos", padx=34, pady=20, command=button_cos)
button_tan = tk.Button(root, text="tan", padx=34, pady=20, command=button_tan)

# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_power.grid(row=7, column=0)
button_log.grid(row=7, column=1)
button_exp.grid(row=7, column=2)
button_sin.grid(row=8, column=0)
button_cos.grid(row=8, column=1)
button_tan.grid(row=8, column=2)

root.mainloop()

