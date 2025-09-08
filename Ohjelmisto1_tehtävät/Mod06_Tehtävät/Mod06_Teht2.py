#tehtävä 2

import random
annettu_numero=int(input('Anna nopan maksimi silmäluku: '))

def nopan_heitto():
    return random.randint(1,annettu_numero)

while True:
    numero = nopan_heitto()
    print('Nopan silmäluku: ', numero)
    if numero ==annettu_numero:
        print('Kone arpoi maksimi silmäluvun!')
        break