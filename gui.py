from tkinter import *
import main

solver = main.WordleSolver()

def solve():
    letter1 = e1.get()
    e1.delete(0, END)
    letter2 = e2.get()
    e2.delete(0, END)
    letter3 = e3.get()
    e3.delete(0, END)
    letter4 = e4.get()
    e4.delete(0, END)
    letter5 = e5.get()
    e5.delete(0, END)
    v1 = var1.get()
    v2 = var2.get()
    v3 = var3.get()
    v4 = var4.get()
    v5 = var5.get()

    var1.set(None)
    var2.set(None)
    var3.set(None)
    var4.set(None)
    var5.set(None)

    match v1:
        case 1:
            solver.delete_word(letter1)
        case 2:
            solver.not_at_pos(letter1, 1)
        case 3:
            solver.at_pos(letter1, 1)

    match v2:
        case 1:
            solver.delete_word(letter2)
        case 2:
            solver.not_at_pos(letter2, 2)
        case 3:
            solver.at_pos(letter2, 2)

    match v3:
        case 1:
            solver.delete_word(letter3)
        case 2:
            solver.not_at_pos(letter3, 3)
        case 3:
            solver.at_pos(letter3, 3)

    match v4:
        case 1:
            solver.delete_word(letter4)
        case 2:
            solver.not_at_pos(letter4, 4)
        case 3:
            solver.at_pos(letter4, 4)

    match v5:
        case 1:
            solver.delete_word(letter5)
        case 2:
            solver.not_at_pos(letter5, 5)
        case 3:
            solver.at_pos(letter5, 5)

    recommended_word["text"] = solver.get_word_rec()

master = Tk()
master.geometry("500x500")
master.title("Wordle Solver")
e1 = Entry(master)
e1.place(x=40, y=100, width= 15)
e2 = Entry(master)
e2.place(x=80, y=100, width= 15)
e3 = Entry(master)
e3.place(x=120, y=100, width= 15)
e4 = Entry(master)
e4.place(x=160, y=100, width= 15)
e5 = Entry(master)
e5.place(x=200, y=100, width= 15)


var1 = IntVar()
Radiobutton(master, text="B", variable=var1, value=1).place(x=30, y=120)
Radiobutton(master, text="Y", variable=var1, value=2).place(x=30, y=140)
Radiobutton(master, text="G", variable=var1, value=3).place(x=30, y=160)

var2 = IntVar()
Radiobutton(master, text="B", variable=var2, value=1).place(x=70, y=120)
Radiobutton(master, text="Y", variable=var2, value=2).place(x=70, y=140)
Radiobutton(master, text="G", variable=var2, value=3).place(x=70, y=160)

var3 = IntVar()
Radiobutton(master, text="B", variable=var3, value=1).place(x=110, y=120)
Radiobutton(master, text="Y", variable=var3, value=2).place(x=110, y=140)
Radiobutton(master, text="G", variable=var3, value=3).place(x=110, y=160)

var4 = IntVar()
Radiobutton(master, text="B", variable=var4, value=1).place(x=150, y=120)
Radiobutton(master, text="Y", variable=var4, value=2).place(x=150, y=140)
Radiobutton(master, text="G", variable=var4, value=3).place(x=150, y=160)

var5 = IntVar()
Radiobutton(master, text="B", variable=var5, value=1).place(x=190, y=120)
Radiobutton(master, text="Y", variable=var5, value=2).place(x=190, y=140)
Radiobutton(master, text="G", variable=var5, value=3).place(x=190, y=160)

btn_get_word = Button(
    master=master,
    text="Get Word",
    command= solve
)
btn_get_word.place(x=110, y=200)

recommended_word = Label(master=master,font=("arial", 16), text="Recommended Word")
recommended_word.place(x=200, y=200)
master.mainloop()

