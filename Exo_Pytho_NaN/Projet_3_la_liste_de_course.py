import sys
import json



def save(items=[]):
    with open('courses.json','w') as f:
        s = json.dumps(items)
        f.write(s)


file = open("courses.json","a+")
r = file.read()

try:
    courses = json.loads(r)
except:
    courses = []

 # choisi une option
user_entrer = int(input("""
    Choisissez parmis les 3 options suivant:
    1 - Ajoutez un élément à la liste 
    2 - Retirer un élément de la liste
    3 - Afficher les éléments de la liste  
    ? Votre choix : """
))

# si l'entrer est incorrect
if not 1 <= user_entrer <= 3:
    print("Veuillez choisir une option valide")

# execution en fonction de l'entrer
if user_entrer == 1:
    elem_ajouter = input("Entrer votre elelment ")
    courses.append(elem_ajouter)
    print(f"L'élément {elem_ajouter} à bien été ajouté")
    print(courses)
    save(courses)
elif user_entrer == 2:
    elem_sup = input("Entrer votre élément à retirer ")
    if elem_sup in courses:
        courses.remove(elem_sup)
        print(f"L'élément {elem_sup} à bien supprimer de la liste")
        print(courses)
        save(courses)
    else:
        print(f"L'élément {elem_sup} n'est pas dans la liste")
elif user_entrer == 3:
    if courses:
        for i,item in enumerate(courses,1):
            print(f"{i}.{item}")
    else:
        print("La liste est vide ")
else:
    print("Code")