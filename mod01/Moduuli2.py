import math
import random

#tehtävä 1
user=input('Hei,kirjoita nimesi tähä:')
print('Hei '+user+'!')

#tehtävä 2

arvo1 = float(input('Ilmoita ympyrän sade:'))
print(f'Ympyrän pinta-ala:{math.pi*arvo1**2:.2f}')

#tehtävä 3

kolmion_kanta=float(input('ilmoita kolmion kannan pituus:'))
kolmion_korkeus=float(input('ilmoita kolmion korkeus:'))
kolmion_hypotenuusa=math.sqrt(kolmion_kanta**2+kolmion_korkeus**2)
print(f'kolmion piiri: {kolmion_kanta+kolmion_korkeus+kolmion_hypotenuusa:.2f}'f'\nkolmion pinta-ala: {kolmion_kanta*kolmion_korkeus/2}')

#tehtävä 4

luku1=float(input('anna luku:'))
luku2=float(input('anna toinen luku:'))
luku3=float(input('anna kolmas luku:'))

print(f'lukujen summa: {luku1+luku2+luku3}'f'\nlukujen tulo: {luku1*luku2*luku3}' f'\nlukujen keskiarvo: {(luku1+luku2+luku3)/3:.2f}')


#tehtävä 5

paino1=float(input('Leivisköjen määrä:'))
paino2=float(input('Naulojen määrä:'))
paino3=float(input('Luotien määrä:'))
Numero1=float(1)

paino_kiloina= paino1 * 8.5 + paino2 * 0.42505 + paino3 * 0.01328281
paino_kokonaisosa= paino_kiloina//Numero1
jakojaannos=paino_kiloina-paino_kokonaisosa
grammat=float(jakojaannos*1000)
print(f'{paino_kokonaisosa:.0f}kg ja 'f'{grammat:.2f}g')

#tehtävä 6

print(
f'sattumanvarainen nelinumeroinen koodi:{random.randint(1,9), random.randint(1,9), random.randint(1,9), random.randint(1,9)}'
f'\nsattumanvarainen kolminumeroinen koodi{random.randint(1,6), random.randint(1,6), random.randint(1,6),}')

