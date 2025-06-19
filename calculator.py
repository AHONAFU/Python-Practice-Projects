import tkinter
from tkinter import *
from tkinter import messagebox

val = ""
a = 0
operator = ""


def btn0_isclicked():
    global val
    val = val + "0"
    data.set(val)


def btn1_isclicked():
    global val
    val = val + "1"
    data.set(val)


def btn2_isclicked():
    global val
    val = val + "2"
    data.set(val)


def btn3_isclicked():
    global val
    val = val + "3"
    data.set(val)


def btn4_isclicked():
    global val
    val = val + "4"
    data.set(val)


def btn5_isclicked():
    global val
    val = val + "5"
    data.set(val)


def btn6_isclicked():
    global val
    val = val + "6"
    data.set(val)


def btn7_isclicked():
    global val
    val = val + "7"
    data.set(val)


def btn8_isclicked():
    global val
    val = val + "8"
    data.set(val)


def btn9_isclicked():
    global val
    val = val + "9"
    data.set(val)


def btn_plus_isclicked():
    global a
    global operator
    global val
    a = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)


def btn_minus_isclicked():
    global a
    global operator
    global val
    a = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)


def btn_multiply_isclicked():
    global a
    global operator
    global val
    a = int(val)
    operator = "x"
    val = val + "x"
    data.set(val)


def btn_divide_isclicked():
    global a
    global operator
    global val
    a = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)


def c_isclicked():
    global a
    global operator
    global val
    val = ""
    a = 0
    operator = ""
    data.set(val)


def calculate():
    global a
    global operator
    global val
    val_2 = val
    if operator == "+":
        b = int((val_2.split("+")[1]))
        result = a + b
        data.set(result)
        val = str(result)
    elif operator == "-":
        b = int((val_2.split("-")[1]))
        result = a - b
        data.set(result)
        val = str(result)
    elif operator == "x":
        b = int((val_2.split("x")[1]))
        result = a * b
        data.set(result)
        val = str(result)
    elif operator == "/":
        b = int((val_2.split("/")[1]))
        if b == 0:
            messagebox.showerror("Error", "Division by 0 not supported")
            a = ""
            val = ""
            data.set(val)
        else:
            result = a / b
            data.set(result)
            val = str(result)


root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0, 0)
root.title("Calculator")

data = StringVar()
lbl = Label(
    root,
    text="This is a label",
    anchor=SE,
    font=("Roboto Light", 20),
    textvariable=data
)
lbl.pack(expand=True, fill="both")

btnrow1 = Frame(root)
btnrow1.pack(expand=True, fill="both")

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both")

btn1 = Button(
    btnrow1,
    text=" 1",
    font=("Roboto Light", 20),
    relief=GROOVE,
    border=0,
    activebackground="#D3D3D3",
    command=btn1_isclicked,
)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(
    btnrow1,
    text="2",
    font=("Roboto Light", 20),
    relief=GROOVE,
    border=0,
    activebackground="#D3D3D3",
    command=btn2_isclicked,
)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(
    btnrow1,
    text="3",
    font=("Roboto Light", 20),
    relief=GROOVE,
    border=0,
    activebackground="#D3D3D3",
    command=btn3_isclicked,
)
btn3.pack(side=LEFT, expand=True, fill="both")

btn_plus = Button(
    btnrow1,
    text="+",
    font=("Roboto Light", 20),
    relief=GROOVE,
    border=0,
    activebackground="#D3D3D3",
    command=btn_plus_isclicked,
)
btn_plus.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(
    btnrow2,
    text=" 4",
    font=("Roboto Light", 20),
    relief=GROOVE,
    border=0,
    activebackground="#D3D3D3",
    command=btn4_isclicked,
)
btn4.pack(side=LEFT, expand=True, fill="both")

btn5 = Button(
    btnrow2,
    text="5",
    font=("Roboto Light", 20),
    relief=GROOVE,
    border=0,
    activebackground="#D3D3D3",
    command=btn5_isclicked,
)
btn5.pack(side=LEFT, expand=True, fill="both")

btn6 = Button(
    btnrow2,
    text="6",
    font=("Roboto Light", 20),
    relief=GROOVE,
    border=0,
    activebackground="#D3D3D3",
    command=btn6_isclicked,
)
btn6.pack(side=LEFT, expand=True, fill="both")

btn_minus = Button(
    btnrow2,
    text=" -",
    font=("Roboto Light", 20),
    relief=GROOVE,
    border=0,
    activebackground="#D3D3D3",
    command=btn_minus_isclicked,
)
btn_minus.pack(side=LEFT, expand=True, fill="both")

btn7 = Button(
    btnrow3,
    text=" 7",
    font=("Roboto Light", 20),
    relief=GROOVE,
    border=0,
    activebackground="#D3D3D3",
    command=btn7_isclicked,
)
btn7.pack(side=LEFT, expand=True, fill="both")

btn8 = Button(
    btnrow3,
    text="8",
    font=("Roboto Light", 20),
    relief=GROOVE,
    border=0,
    activebackground="#D3D3D3",
    command=btn8_isclicked,
)
btn8.pack(side=LEFT, expand=True, fill="both")

btn9 = Button(
    btnrow3,
    text="9",
    font=("Roboto Light", 20),
    relief=GROOVE,
    border=0,
    activebackground="#D3D3D3",
    command=btn9_isclicked,
)
btn9.pack(side=LEFT, expand=True, fill="both")

btn_multiply = Button(
    btnrow3,
    text="X",
    font=("Roboto Light", 20),
    relief=GROOVE,
    border=0,
    activebackground="#D3D3D3",
    command=btn_multiply_isclicked,
)
btn_multiply.pack(side=LEFT, expand=True, fill="both")

btn_clear = Button(
    btnrow4,
    text="C",
    font=("Roboto Light", 20),
    relief=GROOVE,
    border=0,
    activebackground="#D3D3D3",
    command=c_isclicked,
)
btn_clear.pack(side=LEFT, expand=True, fill="both")

btn0 = Button(
    btnrow4,
    text="0",
    font=("Roboto Light", 20),
    relief=GROOVE,
    border=0,
    activebackground="#D3D3D3",
    command=btn0_isclicked,
)
btn0.pack(side=LEFT, expand=True, fill="both")

btn_equal = Button(
    btnrow4,
    text="=",
    font=("Roboto Light", 20),
    relief=GROOVE,
    border=0,
    activebackground="#D3D3D3",
    command=calculate,
)
btn_equal.pack(side=LEFT, expand=True, fill="both")

btn_divide = Button(
    btnrow4,
    text="/",
    font=("Roboto Light", 20),
    relief=GROOVE,
    border=0,
    activebackground="#D3D3D3",
    command=btn_divide_isclicked,
)
btn_divide.pack(side=LEFT, expand=True, fill="both")

mainloop()
