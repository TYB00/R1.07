Base = 4
Fromages = 800
eau = 2
ail = 2
pain = 400

nbconvies = int(input("Entrez le nombre de personnes conviées à la fondue : "))
print("Pour une fondue de ", nbconvies,  "il vous faut :")
print(f"- {Fromages * nbconvies / Base} gr de fromages")
print(f"- {eau * nbconvies / Base} litre d'eau")
print(f"- {ail * nbconvies / Base} gr d'ail")
print(f"- {pain * nbconvies / Base} gr de pain")