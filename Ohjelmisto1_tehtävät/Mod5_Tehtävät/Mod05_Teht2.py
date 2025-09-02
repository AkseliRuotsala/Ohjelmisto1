#tehtävä 2

luvut= []
vastaus = input('Anna luku, tyhjä lopettaa: ')

while vastaus !='':
    print(vastaus)
    luvut.append(int(vastaus ))
    vastaus = input('Anna luku, tyhjä lopettaa: ')
luvut.sort(reverse=True)
print(luvut)