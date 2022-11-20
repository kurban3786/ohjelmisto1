import random
number_amount=int(input("number"))
total_numbers=int(input("total"))

def create_lottery_row(number_amount, total_numbers):
    row = []
    for i in range(number_amount):
        rndNum = random.randint(1, total_numbers)
        while row.count(rndNum) > 0:
            rndNum = random.randint(1, total_numbers)
        row.append(rndNum)
        print(f"{i+1}. nro: {rndNum}")
    row.sort()
    return row

myRow = create_lottery_row(number_amount, total_numbers)
print("Lottorivi:", myRow)