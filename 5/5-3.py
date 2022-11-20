numero = int(input("anna numero : "))
if numero > 1:

    for i in range(2, numero):
        if (numero % i) == 0:
            print(numero, " ei o alkuluku.")
            break
    else:
        print(numero, " alkuluku.")

else:
    print(numero, " ei o alkuluku.")