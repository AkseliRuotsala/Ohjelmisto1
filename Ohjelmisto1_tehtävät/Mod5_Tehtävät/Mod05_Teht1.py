import random
#tehtävä 1

n1=int(input('Anna arpakutioiden määrä: '))
nopat= []
for i in range(n1):
    noppa= random.randint(1,6)
    print(f'Heitit tällä kierroksella luvun: {noppa}')
    nopat.append(noppa)
noppien_summa=sum(nopat)
print(f'Noppien silmälukujen summa:{noppien_summa}')