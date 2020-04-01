inv = False
iten = ["espada", "escudo"]
print("o que você faz")
com = input()
if com == "inventario":
    inv = True
    while inv:
        print(iten)
        print("o que você vai fazer")
        com = input()
        if com == "espada":
            print("Checar ou usar")
            com = input()
            if com == "checar":
                print("uma velha amiga, esteve com você pelos altos e baixos")
                print("                   Voltar?")
                com = input()
                if com == "voltar":
                    inv = True
                else:
                    break
        if com == "escudo":
            print("Checar ou usar")
            com = input()
            if com == "checar":
                print("é novo em folha, confiavel, você ainda não sabe")
                print("                   Voltar?")
                com = input()
                if com == "voltar":
                    inv = True
                else:
                    break
