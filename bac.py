#par Elwan Chollet 22
import random
o=True
a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print("1-Lettre random ")
print("2-Jeu")
n=int(input(""))

if n==1 :
  d=random.choice(a)
  print(d)
  a.remove(d)
if n==2 :
  print("Quelle lettre ?") 
  lettre=input("")
  print("Prenom en",lettre)
  prenom=input("")
  print("Geographie en",lettre)
  geo=input("")
  print("Animal en",lettre)
  animal=input("")
  print("Fruit/legumes en",lettre)
  bouffe=input("")
  print("Metier en",lettre)
  metier=input("")
  print("Objet en",lettre)
  obj=input("")
  print("Cinema en",lettre)
  cinema=input("")
  print("Marque en",lettre)
  marque=input("")
  m=input("Reveal ?")
  if m=="o" :
   print("Prenom : ",prenom)
   print("Geo : ",geo)
   print("Animal : ",animal)
   print("fruit/leg : ",bouffe)
   print("Metier : ",metier)
   print("Objet : ",obj)
   print("Cinema : ",cinema)
   print("Marque : ",marque)