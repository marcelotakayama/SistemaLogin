# Fazendo a importação das bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# Comando utilizado para fazer a criação da janela
jan = Tk()
jan.title('DP Systems - Access Panel')
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)


# Carregando imagens
logo = PhotoImage(file="icons/logo.png")


# Comandos utilizados para estilizar a janela
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)


LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width = 30)
UserEntry.place(x=175, y=100)


jan.mainloop()