numbers = []
input1 = ""
while True:
    try:
        input1 = float(input("Syötä numero: "))
    except ValueError:
        if input1 == "":
            print("Exiting game.")
            break
    else:
        numbers.append(input1)
        input1 = ""

numbers.sort()
print("biggest", numbers[0])
print("smallest", numbers[-1])
