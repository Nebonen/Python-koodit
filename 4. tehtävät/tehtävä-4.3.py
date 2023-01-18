luvut = []
while True:
    luku = input("Anna luku, tyhjä merkkijono lopettaa: ")
    if(luku == ""):
        luvut.sort()
        print(f"Pienin luku: {luvut[0]}")
        print(f"Suurin luku: {luvut[-1]}")
        break
    numero = int(luku)
    luvut.append(numero)