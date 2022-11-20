sukupuoli = input("biologisen sukupuolen? mies/nainen")
hemoglobiiniarvon = float(input("hemoglobiiniarvon?"))
if sukupuoli == "mies" and 134 <= hemoglobiiniarvon <= 195:
    print("oot normali")
elif sukupuoli == "mies" and hemoglobiiniarvon < 134:
    print("alle")
elif sukupuoli == "mies" and hemoglobiiniarvon > 195:
    print("et normali yli")
if sukupuoli == "nainen" and 117 <= hemoglobiiniarvon <= 175:
    print("oot normali")
if sukupuoli == "nainen" and hemoglobiiniarvon < 117:
    print("alle n")
if sukupuoli == "nainen" and hemoglobiiniarvon > 175:
    print("et normali yli n")

