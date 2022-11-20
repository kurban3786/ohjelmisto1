import random

a = None


def nopa():
    global a
    while a != 6:
        a = random.randint(1, 6)
        print(a)


nopa()
