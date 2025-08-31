#tehtävä 1

kala=float(37)
kalan_pituus=float(input('ilmoita kuhan pituus:'))
if kalan_pituus >= kala:
    print('voit pitää kalan')
else:
    print(f'Kuha on {37-kalan_pituus:.2f}cm liian lyhyt. Laske kuha takaisin järveen!')

#tehtävä 2

luokka1='Lux'
luokka2='A'
luokka3='B'
luokka4='C'
input_luokka=input(f'Ilmoita hyttiluokkasi! (Lux, A, B tai C): ')
if input_luokka==luokka1:
    print('LUX on parvekkeellinen hytti yläkannella.')
elif input_luokka==luokka2:
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif input_luokka==luokka3:
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif input_luokka==luokka4:
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Virheellinen hyttiluokka')

#tehtävä 3

sukupuoli1='mies'
sukupuoli2='nainen'
sukupuoli=input('Biologinen sukupuolesi:')

if sukupuoli==sukupuoli1:
    hemoglobiini_muuttuja = int(input('Anna hemoglobiini arvosi(g/L): '))
    if hemoglobiini_muuttuja<134:
        print('Hemoglobiinisi on alhainen')
    elif hemoglobiini_muuttuja>195:
        print('Hemoglobiinisi on korkea')
    else:
        print('Hemoglobiinisi on normaali')
if sukupuoli==sukupuoli2:
    hemoglobiini_muuttuja = int(input('Anna hemoglobiini arvosi(g/L): '))
    if hemoglobiini_muuttuja<117:
        print('Hemoglobiinisi on alhainen')
    elif hemoglobiini_muuttuja>174:
        print('Hemoglobiinisi on korkea')
    else :
        print('Hemoglobiinisi on normaali')

#tehtävä 4
vuosi1=int(input('Ilmoita vuosi:'))

if vuosi1 % 3 !=0:
    print(f'{vuosi1} ei ole karkausvuosi')
else:
    if vuosi1 % 100!=0:
        print(f'{vuosi1} on karkausvuosi')
    else:
        if vuosi1 % 400==0:
            print(f'{vuosi1} on karkausvuosi')
        else:
            print(f'{vuosi1} ei ole karkausvuosi')

