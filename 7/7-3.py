def valitse():
    print("1 - syötä uusi")
    print("2 - haku")
    print("0 - lopetus")
    valinta = -1
    while valinta < 0 or valinta > 2:
        valinta = int(input("valitse: "))
    return valinta

def lisääUusi():
    icao = input("aseman icao-koodi :")
    nimi = input("aseman nimi :")
    lentoasemat[icao] = nimi

def hae():
    icao = input("aseman icao - koodä :")
    if icao in lentoasemat:
        print(lentoasemat[icao])
    else:
        print("tuntematon")

lentoasemat = {}
valinta = valitse()
while valinta !=0:
    if valinta ==1:
        lisääUusi()
    elif valinta == 2:
        hae()
    valinta = valitse()