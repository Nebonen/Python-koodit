def muunto(gallonat):
    litrat = gallonat * 3.785
    print(f'Gallonat litroina: {litrat}')
    return

gallonat = int(input('Montako gallonaa? '))
while gallonat > 0:
    gallonat = int(input('Montako gallonaa? '))
    muunto(gallonat)
    if gallonat < 0:
        break
