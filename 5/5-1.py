import random

dice_amount = int(input("Montakohan arpakuutiotta heitetään?: "))
rolls = []
for i in range(dice_amount):
    rolls.append(random.randint(1, 6))

sum_value = sum(rolls)
print(sum_value)
