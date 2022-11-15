print("Hei maailma!")



pituus = float(input("kuinka pitkä olet?"))
# if 1.5=<pituus<=2:
 # print("Voit ostaa latten.")
if pituus<=2 and pituus>=1.5:
 print("ot noormali!")
if pituus<1.5 or pituus>2:
 print("et noormali!")


mjono1 = input("2f")
mjono2 = input("2f")
if mjono1 == mjono2:
 print("ibhfgiewrfbi")

 muuttuja = 5
 # int-tyyppänn. koska sinne sijoitettin kokonIlaku 5

 muutuja2 = 1.49
 # float/double tyyppänen , koska sinne sijoitetton desimaaliluku

 muuttuja3 = "rakas"
 # string ´´yyppinen, koska sinne sijoitettin merkkijono

 muuttuja4 = input("kirjoita numero")
 # string tyyppinen , jos haluta vertaille suuruutta tai laskee pitää


ika = int(input("mikä ikä ot ?"))
if ika >=15 and ika < 18:
    paino = float(input("anna painosi"))
if ika >=18 or (paino >55 and ika >=15):
    print("hyvä")
# jos anna alle 15 error jos ansin kirjoita paino suljen sisaan