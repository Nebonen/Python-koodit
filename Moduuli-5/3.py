luku = int(input('Anna kokonaisluku: '))

if luku > 1:
    for i in range(2, int(luku/2)+1):
        if (luku % i) == 0:
            print(f'{luku} ei ole alkuluku.')
            break
    else:
        print(f'{luku} on alkuluku.')
else:
    print(f'{luku} ei ole alkululu.')
