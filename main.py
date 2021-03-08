from tkinter import *
import tkinter.messagebox

expertion = ''


def press(index):
    global expertion

    expertion = expertion + str(index)

    equaltion.set(expertion)


def clear():
    global expertion

    expertion = " "

    equaltion.set(expertion)


def equal():
    global expertion

    equlasum = str(eval(expertion))

    equaltion.set(equlasum)


if __name__ == "__main__":
    window = Tk()

    window.resizable(width=False, height=False)

    window.title("Calculator")

    equaltion = StringVar()

    EntryQuestion = Entry(window, width=29, textvariable=equaltion)
    EntryQuestion.grid(row=0, column=0, ipady=8, columnspan=4)

    btnClear = Button(window, text="C", width=24,
                      height=3, command=lambda: clear())
    btnClear.grid(row=1, column=0, columnspan=4)

    btn9 = Button(window, text="9", width=5,
                  height=3, command=lambda: press(9))
    btn9.grid(row=2, column=0)

    btn8 = Button(window, text="8", width=5,
                  height=3, command=lambda: press(8))
    btn8.grid(row=2, column=1)

    btn7 = Button(window, text="7", width=5,
                  height=3, command=lambda: press(7))
    btn7.grid(row=2, column=2)

    btn6 = Button(window, text="6", width=5,
                  height=3, command=lambda: press(6))
    btn6.grid(row=3, column=0)

    btn5 = Button(window, text="5", width=5,
                  height=3, command=lambda: press(5))
    btn5.grid(row=3, column=1)

    btn4 = Button(window, text="4", width=5,
                  height=3, command=lambda: press(4))
    btn4.grid(row=3, column=2)

    btn3 = Button(window, text="3", width=5,
                  height=3, command=lambda: press(3))
    btn3.grid(row=4, column=0)

    btn2 = Button(window, text="2", width=5,
                  height=3, command=lambda: press(2))
    btn2.grid(row=4, column=1)

    btn1 = Button(window, text="1", width=5,
                  height=3, command=lambda: press(1))
    btn1.grid(row=4, column=2)

    btn0 = Button(window, text="0", width=5,
                  height=3, command=lambda: press(0))
    btn0.grid(row=5, column=1)

    btnD = Button(window, text=".", width=5,
                  height=3, command=lambda: press("."))
    btnD.grid(row=5, column=2)

    btnEqual = Button(window, text="=", width=5,
                      height=3, command=lambda: equal())
    btnEqual.grid(row=5, column=0)

    btnDivide = Button(window, text="/", width=5,
                       height=3, command=lambda: press('/'))
    btnDivide.grid(row=2, column=3)

    btnPlus = Button(window, text="+", width=5,
                     height=3, command=lambda: press('+'))
    btnPlus.grid(row=3, column=3)

    btnMinus = Button(window, text="-", width=5,
                      height=3, command=lambda: press('-'))
    btnMinus.grid(row=4, column=3)

    btnMultiple = Button(window, text="*", width=5,
                         height=3, command=lambda: press('*'))
    btnMultiple.grid(row=5, column=3)

    window.mainloop()