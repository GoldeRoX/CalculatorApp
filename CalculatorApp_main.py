import math as m
from tkinter import *


root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=1, columnspan=3, padx=10, pady=10)




def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear1():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addicion"
    f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)


    if math == "addicion":
        e.insert(0, f_num + float(second_number))
    elif math == "subbtraction":
        e.insert(0, f_num - float(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * float(second_number))
    elif math == "division":
        e.insert(0, f_num / float(second_number))



def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subbtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_pow():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
    e.insert(0, f_num ** 2)

def button_root():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
    Button(bg="#ded6d3")
    e.insert(0, m.sqrt(f_num))

def button_sign():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
    final = f_num - f_num - f_num
    e.insert(0, final)


button_1 = Button(root, text="1", bg="#c4bfbd", padx=35, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", bg="#c4bfbd", padx=35, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", bg="#c4bfbd", padx=35, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", bg="#c4bfbd", padx=35, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", bg="#c4bfbd", padx=35, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", bg="#c4bfbd", padx=35, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", bg="#c4bfbd", padx=35, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", bg="#c4bfbd", padx=35, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", bg="#c4bfbd", padx=35, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", bg="#c4bfbd", padx=36, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", bg="#94908e", padx=28, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=70, pady=20,bg="#05B3CB", fg="#ffffff", command=button_equal)
button_clear = Button(root, text="C", bg="#94908e", padx=28, pady=20, command=lambda: button_clear1())
button_pow = Button(root, text="X^2", bg="#94908e", padx=30, pady=20, command=button_pow)
button_root = Button(root, text="√", bg="#94908e", padx=35, pady=20, command=button_root)
button_sign = Button(root, text="+/-", padx=28, pady=20, command=button_sign)


button_subtract = Button(root, text="-", bg="#94908e", padx=28, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", bg="#94908e", padx=28, pady=20, command=button_multiply)
button_divide = Button(root, text="/", bg="#94908e", padx=35, pady=20, command=button_divide)


#  bg="#c4bfbd",

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=1)
button_clear.grid(row=1, column=3)
button_add.grid(row=4, column=3)
button_equal.grid(row=5, column=2, columnspan=2)

button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=2)

button_pow.grid(row=1, column=1)
button_root.grid(row=1, column=0)
button_sign.grid(row=5, column=0)





root.mainloop()
