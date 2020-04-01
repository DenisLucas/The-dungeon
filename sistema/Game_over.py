rec = False
while not rec:
    print("morte chega a todos")
    print("Você deseja tentar denovo?")
    print('y/n')
    res = input()
    if res == "y":
        print("Você reencarna")
        import mapa.sala01
    else:
        print("boms sonhos")
        rec = True
