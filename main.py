from tkinter import *
from tkinter import ttk
Root = Tk()
Str = StringVar()
Str = "What has 4 legs?"
Str1 = StringVar()
Str1 = "What is the most famous Search Engine?"
V = IntVar()
V1 = IntVar()
def Submit():
    Value = int(V.get())
    print(Value)
    if Value == 0:
        Str = "Correct!"
        L1 = Label(F1, text=Str)
        L1.pack()
    else:
        Str = "Incorrect!"
        L1 = Label(F1, text=Str)
        L1.pack()
def Submit1():
    Value = int(V1.get())
    print(Value)
    if Value == 0:
        Str1 = "Correct!"
        L2 = Label(F1, text=Str)
        L2.pack()
    else:
        Str1 = "Incorrect!"
        L2 = Label(F1, text=Str)
        L2.pack()
def Submit2():
    Value = int(V.get())
    print(Value)
    if Value == 0:
        Str = "Correct!"
        L3 = Label(F1, text=Str)
        L3.pack()
    else:
        Str = "Incorrect!"
        L3 = Label(F1, text=Str)
        L3.pack()
Root.title("Quiz")
notebook = ttk.Notebook(Root)
F1 = Frame(notebook)
notebook.add(F1, text="Q1")
Radio = Radiobutton(F1, text="Horse", variable=V, value=0)
Radio1 = Radiobutton(F1, text="Human", variable=V, value=1)
Radio2 = Radiobutton(F1, text="Dragonfly", variable=V, value=2)
label = Label(F1, text=Str)
Button = Button(F1, text="Submit", command=Submit)
label.pack()
Radio.pack()
Radio1.pack()
Radio2.pack()
Button.pack()
notebook.pack()
Root.mainloop()
