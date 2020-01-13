# Fazendo a importação das bibliotecas
from tkinter import *
from tkinter import messagebox

jan = Tk()
jan.title('DP Systems - Access Panel')
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)

LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")


jan.mainloop()