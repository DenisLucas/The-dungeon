# biblioteca de dados aleatorios para os dados
import random
# variaveis globais
Hp = 100
fugir = False
batalha = True
Mhp = 100
ato = str
# loop enquanto booleano batalha estiver verdadeiro
while batalha:
    # caso o per não fugiu antes uma frase caso tentou, outra
    if not fugir:
        print("Você é emboscado por um esqueleto faminto, ele avança em sua direção o que você faz")
        ato = input()
    else:
        print("O que vai fazer")
        ato = input()
        # se o ato foi escrito atacar
    if ato == "atacar":
        fugir = True
        dados = random.randint(1, 21)
        str(dados)
        if dados >= 10:
            print("você atingiu a criatura")
            Mhp = int(Mhp) - 50
            print(Mhp)
            print(dados)
        if dados < 10:
            print("você foi atacado")
            Hp = int(Hp) - 50
            print(Hp)
            print(dados)
    if Hp <= 0:
        print("você morreu")
        batalha = False
    if Mhp <= 0:
        batalha = False
        print("Vitoria")
        # se ato foi escrito fugir
    if ato == "fugir":
        dados = random.randint(1, 21)
        str(dados)
        if dados > 10:
            print("você fugiu com sucesso")
            Mhp = int(Mhp) - 100
            batalha = False
        else:
            print("você não fugiu")
            if dados >= 10:
                print("você atingiu a criatura")
                Mhp = int(Mhp) - 50
                print(Mhp)
                print(dados)
            if dados < 10:
                print("você foi atacado")
                Hp = int(Hp) - 50
                print(Hp)
                fugir = True
                print(dados)
            if Hp <= 0:
                batalha = False
            if Mhp <= 0:
                batalha = False
                print("Vitoria")

ato = "0"



