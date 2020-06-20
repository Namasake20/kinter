from tkinter import *
import math


root = Tk()
root.title("Simple calculator")
e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def sq():
    num1 = m.get() 
    global f_number 
    global op
    op = "sqrt"
    f_number = int(num1)
    m.delete(0,END)

def button_click_more(num):
    curr = m.get()
    m.delete(0,END)
    m.insert(0,str(curr) + str(num))

def button_click(number):
    #e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)
def cls():
    m.delete(0,END)


def eq():
    m.delete(0,END)
    if op == "sqrt":
        m.insert(0,math.sqrt(f_number))
    if op == "cos":
        m.insert(0,math.cos(f_number))
    if op == "tan":
        m.insert(0,math.tan(f_number))
    if op == "sin":
        m.insert(0,math.sin(f_number))


def Cos():
    num1 = m.get() 
    global f_number 
    global op
    op = "cos"
    f_number = int(num1)
    m.delete(0,END)
def Tan():
    num1 = m.get() 
    global f_number 
    global op
    op = "tan"
    f_number = int(num1)
    m.delete(0,END)
def Sin():
    num1 = m.get() 
    global f_number 
    global op
    op = "sin"
    f_number = int(num1)
    m.delete(0,END)



def button_more():
    global m
    more = Tk()
    more.title("Simple calculator")
    m = Entry(more,width=35,borderwidth=5)
    m.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
    button_1 = Button(more,text="1",padx=40,pady=20,command=lambda: button_click_more(1))
    button_2 = Button(more,text="2",padx=40,pady=20,command=lambda: button_click_more(2))
    button_3 = Button(more,text="3",padx=40,pady=20,command=lambda: button_click_more(3))
    button_4 = Button(more,text="4",padx=40,pady=20,command=lambda: button_click_more(4))
    button_5 = Button(more,text="5",padx=40,pady=20,command=lambda: button_click_more(5))
    button_6 = Button(more,text="6",padx=40,pady=20,command=lambda: button_click_more(6))
    button_7 = Button(more,text="7",padx=40,pady=20,command=lambda: button_click_more(7))
    button_8 = Button(more,text="8",padx=40,pady=20,command=lambda: button_click_more(8))
    button_9 = Button(more,text="9",padx=40,pady=20,command=lambda: button_click_more(9))
    button_0 = Button(more,text="0",padx=40,pady=20,command=lambda: button_click_more(0))
    button_cls = Button(more,text="clear",padx=79,pady=20,command=cls)
    button_sq = Button(more,text="sqrt",padx=34,pady=20,command=sq)
    button_eq = Button(more,text="=",padx=91,pady=20,command=eq)

    button_cos = Button(more,text="cos",padx=34,pady=20,command=Cos)
    button_tan = Button(more,text="tan",padx=36,pady=20,command=Tan)
    button_sin = Button(more,text="sin",padx=34,pady=20,command=Sin)


    button_1.grid(row=3,column=0)
    button_2.grid(row=3,column=1)
    button_3.grid(row=3,column=2)

    button_4.grid(row=2,column=0)
    button_5.grid(row=2,column=1)
    button_6.grid(row=2,column=2)

    button_7.grid(row=1,column=0)
    button_8.grid(row=1,column=1)
    button_9.grid(row=1,column=2)

    button_0.grid(row=4,column=0)
    button_cls.grid(row=4,column=1,columnspan=2)
    button_sq.grid(row=5,column=0)


    button_cos.grid(row=6,column=0)
    button_tan.grid(row=6,column=1)
    button_sin.grid(row=6,column=2)

    button_eq.grid(row=5,column=1,columnspan=2)

     


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition" 
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,f_num + int(second_number))
    if math == "subtraction":
        e.insert(0,f_num - int(second_number))
    if math == "multiplication":
        e.insert(0,f_num * int(second_number))
    if math == "division":
        e.insert(0,f_num / int(second_number))


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction" 
    f_num = int(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication" 
    f_num = int(first_number)
    e.delete(0,END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division" 
    f_num = int(first_number)
    e.delete(0,END)


button_1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
button_2 = Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3 = Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
button_4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6 = Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
button_7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
button_9 = Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))
button_add = Button(root,text="+",padx=40,pady=20,command=button_add)
button_more = Button(root,text="AC",padx=36,pady=20,command=button_more)
button_equal = Button(root,text="=",padx=40,pady=20,command=button_equal)
button_clear = Button(root,text="clear",padx=80,pady=20,command=button_clear)

button_subtract = Button(root,text="-",padx=41,pady=20,command=button_subtract)
button_multiply = Button(root,text="x",padx=40,pady=20,command=button_multiply)
button_divide = Button(root,text="/",padx=41,pady=20,command=button_divide)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1)

button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

button_more.grid(row=5,column=2)


root.mainloop()