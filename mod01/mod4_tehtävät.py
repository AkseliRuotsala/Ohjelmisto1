import math
import random

#tehtävä 1

arvo1=1
while arvo1<=100:
    if arvo1 % 3 == 0:
        print(arvo1)
    arvo1 +=1

#tehtävä 2

tuuma=0

while tuuma>= 0:
    tuuma=float(input('Ilmoita pituus tuumina(negativinen arvo lopettaa):'))
    if tuuma >= 0:
        cm= tuuma*2.54
        print(f'{tuuma} tuumaa on {cm:.2f}cm')
    else:
        print('Ohjelma lopetettiin')


#tehtävä 3


#tehtävä 4

rand_num_1=random.randint(1,10)

arvattu_numero=0

while arvattu_numero != rand_num_1:
    arvattu_numero=int(input('Arvaa numero väliltä 1-10:'))
    if  arvattu_numero > rand_num_1:
        print('Liian suuri arvaus')
    elif arvattu_numero < rand_num_1:
        print('Liian pieni arvaus')
    else:
        print('Oikein')
        break


#tehtävä 5

salasana1='ipad'
tunnus1='Iphone'

yrityksiä=0

while yrityksiä<5:
    tunnus2=input('Ilmoita tunnus: ')
    salasana2=input('Ilmoita salasana: ')
    if tunnus2 ==tunnus1 and salasana2 ==salasana1:
        print('Tervetuloa')
        break
    else:
        print('Virheellinen tunnut tai salasana')
        yrityksiä +=1
if yrityksiä==5:
    print('Pääsy evätty')


#tehtävä 6
N = 10
ii = 1
while ii < N:
    ii = ii + 1
    # arvotaan satunnianen piste
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f'arvottu piste:{x},{y}')




