#Tehtävä 6

import math

def pizzalaskin(halkaisija, hinta):
    halkaisija_m=(halkaisija/2)/100
    pinta_ala_m=math.pi*(halkaisija_m**2)
    neliön_hinta=hinta/pinta_ala_m
    return neliön_hinta

pizza1_halkaisija=float(input('Ilmoita pitsan halkaisija (cm): '))
pizza1_hinta=float(input('Ilmoita pitsan hinta: '))


pizza2_halkaisija=float(input('Ilmoita pitsan halkaisija (cm): '))
pizza2_hinta=float(input('Ilmoita pitsan hinta: '))

pizza1_arvo=pizzalaskin(pizza1_halkaisija,pizza1_hinta)
pizza2_arvo=pizzalaskin(pizza2_halkaisija,pizza2_hinta)

print(f'Ensimmäisen pitsan arvo: {pizza1_arvo: .2f}€/m^2')
print(f'Toisen pitsan arvo: {pizza2_arvo: .2f}€/m^2')

if pizza1_arvo < pizza2_arvo:
    print('Ensimmäinen pitsa on kannattavampi hankinta')
if pizza2_arvo < pizza1_arvo:
    print('Toisen pitsa on kannattavampi hankinta')
else:
    print('Molemmat pitsat ovat yhtä arvokkaita')