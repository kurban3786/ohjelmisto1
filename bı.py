ika = int(input("mikä ikä ot ?"))
if ika >=15 and ika < 18:
    paino = float(input("anna painosi"))
if ika >=18 or (ika >= 15 and paino > 55):
    print("hyvä")
else:
    print("lääkkeen käyttö ei ole sallittua")

ika = int(input("mikä ikä ot ?"))
if ika >=15 and ika < 18:
    paino = float(input("anna painosi"))
if ika >=18:
    print("lääken käytte sallittu")
if ika>=15 and ika<18:
    if paino>=55:
        print("lääken käytte sallittu")

ika = int(input("mikä ikä ot ?"))
if ika >=18:
    print("hyvä")
elif ika <15:
    print("lääkkeen käyttö ei ole sallittua")
else:
    paino = float(input("anna painosi"))
    if paino>=55:
        print("lääken käytte sallittu")
    else:
        print("lääkkeen käyttö ei ole sallittua")