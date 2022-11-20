def g_to_l(gallonmaara):
    litramaara = gallonmaara * 3.7854
    return litramaara
gallonmaara = int(input("anna gallon maara"))

while gallonmaara > 0:
    litrat = g_to_l(gallonmaara)
    print("se on ",litrat)
    gallonmaara = int(input("anna gallon maara"))
