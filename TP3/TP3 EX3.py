from random import*
A = randint(0, 100)
B = int(input("Choisissez une valeur entre 0 et 100 : "))
while A != B:
    if A < B:
        print("Le nombre est plus petit")
    else:
        print("Le nombre est plus grand")
    print("Essayez encore")
    B = int(input("Choisissez une valeur entre 0 et 100 : "))
print("Félicitation le nombre était : ",A)