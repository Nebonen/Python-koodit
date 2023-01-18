sukupuoli = input('Anna sinun biologinen sukupuoli: ')
hemoglo = int(input('Anna hemoglobiini arvosi: '))

if sukupuoli == 'nainen' and hemoglo >= 117 and hemoglo <= 175:
    print('Hemoglobiinisi on normaali')
elif sukupuoli == 'nainen' and hemoglo < 117:
    print('Hemoglobiinisi on alhainen')
elif sukupuoli == 'nainen' and hemoglo > 175:
    print('Hemoglobiinisi on korkea')

if sukupuoli == 'mies' and hemoglo >= 134 and hemoglo <= 195:
    print('Hemoglobiinisi on normaali')
elif sukupuoli == 'mise' and hemoglo < 134:
    print('Hemoglobiinisi on alhainen')
elif sukupuoli == 'mies' and hemoglo > 195:
    print('Hemoglobiinisi on korkea')
