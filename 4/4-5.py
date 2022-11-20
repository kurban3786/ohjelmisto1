valid_username = "python"
valid_password = "rules"

tryCount = 0
maxTries = 5
while tryCount < maxTries:
    #tryCount = tryCount +1
    tryCount += 1
    input_username = input("käyttäjätunnus?")
    input_password = input("salsanasi?")
    if valid_username == input_username and valid_password == input_password:
        print("tervetuloa!")
        break
    print("virheelliset kirjautumistiedot, yritä uudelleen!")
else:
    print("pääsy evätty!")
