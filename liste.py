#exo1
""" l=[]
som=0
cont=0
for i in range(5):
    n= int (input("Entrez un nombre: "))
    l.append(n)
    
    cont+=1
som= sum(l)
print(l)
print(f"La somme de ces nombres est: {som}")
print(f"La moyenne de ces nombres est: {som/cont}") """
    
#exo2
""" l=[]
n= int (input("Entrez le nombre de valeurs que vous voulez saisie: "))
maxe=valr= int (input("Entrez une valeur: "))
for i in range(n-1):
    valr= int (input("Entrez une valeur: "))
    l.append(valr)
    if valr > maxe:
        maxe = valr
print(f"Le plus grand de ces valeurs est: {maxe}") """

#exo3
""" l=[0,1,2,3,4,5,6,7,8,9]
n= int (input("Entrez un nombre: "))
if n in l:
    print("Nombre trouvé")
else:    
    print("Nombre non trouvé") """

#exo4
""" compt=0
n = int (input("Combien de nombre voulez-vous saisie: "))
l=[]
for i in range(n):
    valr= int (input("Entrez une valeur: "))
    l.append(valr)
    if valr % 2 == 0:
        compt+=1
print(f"Il y a {compt} nombre pairs dans la liste.") """  
 
#exo5
""" print("Sisiez 5 nombres: ")
l=[]
for i in range(5):
    n= int (input("Saisiez: "))
    l.append(n)
print(l)
print(f"Son inverse: {l[::-1]}") """

#exo7
""" ph= input("Entrez une phrase: ")
print(f"Le nombre de caractères dans cette phrase est: {len(ph)}")
print(f"Le nombre de mots dans cette phrase est: {len(ph.split())}") """

#exo8
""" mot= input("Entrez un mot: ")
vol=["a","e","i","o","u","y"]
comp=0
for i in mot:
    if i in vol:
        comp+=1

print(f"Le nombre de voyelles dans ce mot est: {comp}") """


""" l=[0,1,2,3,4,5,6,7,8,9]

for i in range(len(l)):
    l[i]+=1
    

l.append(11)
l.append(12)
l.append(13)
print(l[0])
print(l[0:2])
print(l[-1])
print(l[-2:])

paires=[]
impaires=[]
[paires.append(i) for i in l if i % 2==0 ]
[impaires.append(i) for i in l if i % 2!=0 ] 
print(paires)
print(impaires)
l.insert(3,3.5)
l.remove(3.5)
print(l.reverse())
n= int (input("Nombre? : "))

if n in l:
    print("Ce nombre est dans la liste") 
else:
    print("Ce nombre n'est pas dans la liste") """

""" s= "Python"
for i in s:
    print(i) """

""" nombres = [2, 5, 8, 3, 10] 
for i in nombres:
    print(i*2)

nmp=[]

for i in nombres:
    if i % 2 ==0:
        nmp.append(i)

print(nmp) """

""" temperatures = [18, 20, 21, 19, 23, 25, 30, 28, 27, 26, 22, 19, 18, 17, 16] 
tempmoy= sum(temperatures)/len(temperatures)
print(f"Température moyenne : {tempmoy:.2f} °C")
tstm=[]
for i in temperatures:
    if i > tempmoy:
        tstm.append(i)

print(f"Les températures supérieures à la moyenne= {tstm} ")

tmpmax=max(temperatures)
print(f"Temperature maximum {tmpmax} °C sont jours le {temperatures.index(tmpmax)}")
temperatures.sort(reverse=True)
print(temperatures)

tmpinfa20= []
for i in temperatures:
    if i < 20:
        tmpinfa20.append(i)

print(tmpinfa20) """

""" langages = ["Python", "JavaScript", "C++", "Java", "Go"] 
langages.append("Rust")
langages.insert(1, "TypeScript")
langages.remove("Java")
print(langages)
langages.sort()
print(langages)
t='t'
for i in langages:
    if t in i:
        print(i) 

a='a'
c=0
for i in langages:
    if a in i:
        c+=1

print(c) """

""" l=['a','b','c',10,11,12,15,20,22,14]
l1=[]
l2=[]
l3=[]
caractere= 'a','b','c'
for i in l:
    if i in caractere:
        l1.append(i)
    elif i % 2 == 0 :
        l2.append(i)
    elif i % 2 != 0:
        l3.append(i)
   
l2.remove(14)
l2.insert(2,14)
print(l1)
print(l2)
print(l3) """