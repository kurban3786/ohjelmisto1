numb = int(input("luku:"))
alkuluku = True

for i in range(2, numb):
    if numb % i == 0: alkuluku = False

if not alkuluku:
    print(f"luku{numb} on alkuluku ")
else:
    print(f"luku {numb} ei ole alkuluku")