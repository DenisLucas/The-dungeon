from tkinter import *

root = Tk()
root.title("The dungeon")


def progresso():
    escolha = str(comands.get())
    comands.delete(0, END)
    if escolha == "iniciar":
        tex.destroy()
        enter.config(command=prot)
        global tex1
        tex1 = Label(root, text="Mas antes.... qual é o seu nome?")
        tex1.grid(column=0, row=0)
        return


def prot():
    global tex1
    global tex2
    heroi = str(comands.get())
    comands.delete(0, END)
    tex1.destroy()
    tex2 = Label(root, text="oh seja bem vindo " + heroi.title())
    tex2.grid(column=0, row=0)
    enter.config(command=cena1, text="continue")
    return


def cena1():
    comands.delete(0, END)
    global tex2
    tex2.destroy()
    tex3 = Label(root, text="""

A luz do sol já não mais tocava sua pele quando você descia as escadarias sombrias de uma dungeon, seus dedos esfregando
nas paredes sujas de pó e plantas que achavam seu caminho por entre rachaduras na parede de concreto. 

 respira o ar, o cheiro de morte e decomposição ataca seu nariz, você faz uma careta, mais alguns passos e 
finalmente chega ao chão, uma sala quadrada, onde o caminho se reparte em três somente iluminada pela luz que esquentava
suas costas 
    """)
    tex4 = Label(root, text="esquerda, direita, reto")
    enter.config(command=rotas1, text="enter")
    tex3.grid(column=0, row=0)
    comands.grid(column=0, row=2)
    enter.grid(column=0, row=3)
    tex4.grid(column=0, row=1)
    return


def rotas1():
    rota = str(comands.get())
    if rota == "esquerda":
        enter.config(command=sala2a())
    if rota == "direita":
        enter.config(command=sala2b())
        comands.delete(0, END)
    if rota == "reto":
        enter.config(command=sala2c())
    return


def sala2a():
    print("sala2a")
    return


def sala2b():
    print("sala2b")
    return


def sala2c():
    print("sala2c")
    return


tex = Label(root, text="quer iniciar o jogo, escreva iniciar")
comands = Entry(root)
enter = Button(root, text="Enter", command=progresso)
tex.grid(column=0, row=0)
comands.grid(column=0, row=1)
enter.grid(column=0, row=2)

root.mainloop()
