#Tehtävä 1
import random

def nopan_heitto():
    return random.randint(1,6)

while True:
    numero = nopan_heitto()
    print('Nopan silmäluku: ', numero)
    if numero ==6:
        break