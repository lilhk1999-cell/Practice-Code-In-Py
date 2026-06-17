""" etudiant={"nom" : "Aly", "âge" : 20 , "note" : 16.5 }
print(etudiant["nom"])
etudiant["âge"]= etudiant["âge"]+5
etudiant["niveau"]="L2"
print(etudiant) """

""" notes={"Ali" : 12, "Salma" : 15, "Zeineb" : 10, "Noura"  : 14 }
for nom,note in notes.items():
    print(nom,note)

print("Les élèves ayant une note supérieure ou égale à 12: ")
for nom,note in notes.items():
    if note >= 12:
        print(nom,note)

notes["Ahmed"]=16
print(notes["Salma"])
notes["Salma"]=notes["Salma"]+2
moy= sum(notes.values())/len(notes)
print(f"La moyenne des notes= {moy}")
del notes["Ali"]
print(notes)
print(f"Le nombre des élèves= {len(notes)}") """

""" inventaire = { 
"bananes": 5000, 
"pommes": 2094, 
"poires": 412809, 
"cerises": 78, 
"ananas": 0 
} 

print("Les fruits dont la quantité est inférieure à 100: ")
for f,q in inventaire.items():
    if q < 100:
        print(f,q)


inventaire["mangues"]=120
inventaire["cerises"]=inventaire["cerises"]+50
for key,value in list(inventaire.items()):
    if value == 0:
        del inventaire[key]

print(inventaire)
max_key=0
for key,value in list(inventaire.items()):
    if value > max_key:
        max_key= value
        keym= key

print(f"le fruit qui a la plus grande quantité: {keym}") """



