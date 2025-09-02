#tehtävä 3

luku1= int(input('anna kokonaisluku, tarkistetaan onko se alkuluku:'))
jaollinen=[]

onko_alkuluku=True

for i in range(2,luku1):
    print(i)
    if luku1 % i ==0:
        onko_alkuluku=False
        jaollinen.append(i)


if onko_alkuluku:
    print(f'{luku1} on alkuluku')
else:
    print(f'{luku1} ei ole alkuluku')
    print(jaollinen)
