#indixé le value d'une clé
'''NaN = {"dt ": "17h", "at" : "08h"}
print(NaN["dt "])'''

#vérifier si une valeur d'une clé est dasns un dictionnaire
'''def diction (NaN , clé) :
    if clé in NaN :
       return True
    else : 
       return False'''

# Manupulation de dictionnaire

stock = {}
continuer = "o"
while continuer == "o" : 
    name = input("Entrer en produit svp : ")
    if name in stock:
        print(stock[name])
        print("1- Supprimer un element\n 2- Ajouter un elemnt\n 3-Videz le stock ")
        menu = input(" : ")
        match menu:
            case "1" : 
                sup = input("Entrer la valeur asuprimer : ")
                stock[name].remove(sup)
            case "2" :
                sup = input("Entrer la a ajouter : ")
                stock[name].update(sup)
            case "3" :
                sup = input("entrer le nom du stock : ")
                stock[name].clear(sup)
    else:
        new_name = input("entrer une nouvelle valeur : ")
        stock[name]=[new_name]
    
