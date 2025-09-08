#tehtävä 3
import math

gallona_maara=True

while gallona_maara:
    muuttuja=(int(input('Gallona määrä (negatiivinen luku sammuttaa muuntimen): ')))
    if muuttuja>=0:
        print(f'Määrä litroina: {muuttuja * 3.785}')
    else:
        print('Muunnin sammutettiin')
        break