numerot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def poista_parittomat(numerot):
    for i in numerot:
       if i % 2 == 0:
        return

karsittuLista = poista_parittomat(numerot)
print(f'Alkuperäinen lista: {numerot}')
print(f'Karsittu lista: {karsittuLista}')
poista_parittomat(numerot)
