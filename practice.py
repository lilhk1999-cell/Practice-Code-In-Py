"""Afficher les diviseurs d’un nombre """
""" n= int (input("Entrez un nombre: "))
for i in range(1,n+1):
    if n % i == 0:
        print(f"{i} est un diviseur de {n}") """

""" Compter le nombre de chiffres d’un entier """
""" comp=0
n= int (input("Entrez un nombre: "))
if n == 0:
    comp=1
    print(f"Ce nombre a {comp} chiffre")
else:
    while(n != 0):
        n = n // 10
        comp+=1

    print(f"Ce nombre a {comp} chiffres") """

""" IVERSER UN NOMBRE """

""" n = int (input("Entrez un nombre: "))
inv=0
while(n != 0):
    d= n % 10
    inv= inv * 10 + d
    n = n // 10

print(f"L'inverse de ce nombre est: {inv}") """

""" n = int (input("Entrez un nombre: "))
m = int (input("Entrez un nombre: "))
if (n < 0 and m > 0) or (n > 0 and m < 0):
    print("Le signe du resultat de la production est négatif")
elif n == 0 or m == 0:
    print("Le resultat de la production est nul")
else:
    print("Le signe du resultat de la production est positif ") """

""" n = int (input("Entrez un nombre: "))
n1 = int (input("Entrez un autre nombre: "))
if n == n1:
    print("Les deux nombres sont egaux")
elif n < n1:
    print("Le plus grand nombre est",n1)
else:
    print("Le plus grand nombre est",n) """
""" min_val = 0
max_val = 0
n = int (input("Entrez un nombre: "))
n1 = int (input("Entrez un autre nombre: "))
print()

if n < n1:
    min_val = n
    max_val = n1
else:    
    min_val = n1
    max_val = n

print("Le plus grand nombre est", max_val)
print("Le plus petit nombre est", min_val) """

""" n = float (input("Entrez un nombre positif: "))
while (n < 0):
    n = float (input("Entrez un nombre positif: "))

print("Merci",n,"est positif") """

""" rng=1
rngmx= rng
mx=0
n = int (input("Entrez un nombre (0 pour arreter): "))
while n != 0:
    if n > mx:
        mx = n
        rngmx = rng
    rng+=1
    n = int (input("Entrez un autre nombre (0 pour arreter): "))

print(f"Le nombre le plus grand est {mx} et sa position est {rngmx}") """

""" Ecrire un programme qui permet de déterminer si un nombre est premier. N.B : Un nombre premier est un 
entier qui n'a que 2 diviseurs : 1 et lui-même. """

""" i=2
n = int (input("Saisir un nombre: "))
if n < 2:
    print(f"{n} n'est pas un nombre premier")
else:
    while i < n:
        if n % i ==0:
            print(f"{n} n'est pas un nombre premier")
            break
        i+=1
    else:
        print(f"{n} est un nombre premier") """

l=[]
n = int (input("Saisir un nombre: "))




