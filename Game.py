from tkinter import *

root = Tk()
root.title("The dungeon")
# root.geometry("600x400")


def progresso():
    escolha = str(comands.get())
    if escolha == "iniciar":
        tex.destroy()
        enter.config(command=prot)
        global tex1
        tex1 = Label(root, text="Mas antes.... qual é o seu nome?")
        tex1.grid(column=0, row=0)
        return


def prot():
    global tex1
    heroi = str(comands.get())
    tex1.destroy()
    tex2 = Label(root, text="oh seja bem vindo " + heroi)
    tex2.grid(column=0, row=0)
    enter.config(command=cena1)
    return


def cena1():
    return



tex = Label(root, text="quer iniciar o jogo, escreva iniciar")
comands = Entry(root)
enter = Button(root, text="Enter", command=progresso)
tex.grid(column=0, row=0)
comands.grid(column=0, row=1)
enter.grid(column=0, row=2)

root.mainloop()
