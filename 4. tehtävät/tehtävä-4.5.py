tunnus = 'python'
salasana = 'rules'
yritykset = 0

while yritykset < 5:
    yritykset = yritykset + 1
    kayt_tunnus = input('Syötä käyttäjätunnus: ')
    kayt_salasana = input('Syötä salasana: ')
    if (kayt_tunnus != tunnus or kayt_salasana != salasana):
        print('Pääsy evätty!')
    else:
        print('Tervetuloa!')
        break
    