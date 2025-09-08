#tehtävä 4

def loppusumma(lista):
    summa=0
    for luku in lista:
        summa=summa+luku
    return summa

arvot=[1,4,22,-71,99]
summa=loppusumma(arvot)
print('Listan lukujen summa: ',summa )