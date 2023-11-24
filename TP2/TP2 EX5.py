x = int(input("Entrez un nombre entier : "))

if x < 0:
    nombre = "négatif" 
else:
    nombre = "positif"

if x == 0:
    nombre = "zéro"

if x%2 == 0:
    identite = "pair"
else:
    identite = "impair"

print("le nombre est ", nombre," et il est ", identite)