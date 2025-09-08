#tehtävä 5

def parittomien_lukujen_poisto(lista):
    return [luku for luku in lista if luku %2==0]

numerolista=(1,2,3,4,5,6,7,8,9)
uusilista=parittomien_lukujen_poisto(numerolista)
print('Lista jossa on kaikki luvut: ', numerolista)
print('Lista jossa on vain parilliset luvut: ', uusilista)
