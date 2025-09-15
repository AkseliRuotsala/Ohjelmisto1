nimet = set()

while True:
    nimi = input("Anna nimi (tyhjä lopettaa): ")
    if nimi == "":  # tyhjä lopettaa
        break
    if nimi in nimet:
        print("Aikaisemmin syötetty nimi")
    else:
        print("Kirjoita uusi nimi")
        nimet.add(nimi)

print("\nAnnetut nimet:")
for n in nimet:
    print(n)