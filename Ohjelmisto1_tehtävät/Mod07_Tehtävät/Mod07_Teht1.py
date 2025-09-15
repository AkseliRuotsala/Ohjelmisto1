vuodenajat = (
    "talvi",
    "talvi",
    "talvi",
    "kevät",
    "kevät",
    "kevät",
    "kesä",
    "kesä",
    "kesä",
    "syksy",
    "syksy",
    "syksy"
)

kuukausi = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kuukausi <= 12:
    vuodenaika = vuodenajat[kuukausi % 12] if kuukausi == 12 else vuodenajat[kuukausi]
    vuodenajat = (
        "talvi",
        "talvi",
        "kevät",
        "kevät",
        "kevät",
        "kesä",
        "kesä",
        "kesä",
        "syksy",
        "syksy",
        "syksy",
        "talvi"
    )
    print("Vuodenaika on:", vuodenajat[kuukausi-1])
else:
    print("Virheellinen kuukauden numero!")