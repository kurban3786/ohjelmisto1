vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")
kuukausi = int(input("Anna kuukauden numemero, niin kerron vuodenajan"))

if kuukausi >= 1 and kuukausi < 4:
    indeksi = 0
elif kuukausi >= 4 and kuukausi < 6:
    indeksi = 1
elif kuukausi >= 6 and kuukausi < 9:
    indeksi = 2
elif kuukausi >= 9 and kuukausi < 13:
    indeksi = 3
else:
    print ("Annoi kelvottoman kuukauden")

print(vuodenajat[indeksi])