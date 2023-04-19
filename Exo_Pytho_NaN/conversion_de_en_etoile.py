
         # convir un mot en etoile

import random
import json

def randomwold () :
    tableau = ['bonjour','maison','étude','voiture']
    return random.choice(tableau)

if __name__ == '__main__' :
    mail = input("Entrer votre mail stp")
    progression = {
        "email" : mail,
        "nombre_de_chance" : 3,
        "level" : {
                    "mot" : randomwold(),
                    "mot_trouver" : ''
        }
    }
    fil = open('progress.json', 'r')
    r = fil.read()
    progressions = json.loads(r)
    for progress in progressions :
       if progress.get('email') == mail :
          progression = progress 
 
    
         #VERIFIER L'INDEX DU CARACTERE DE L'UTILASATEUR
#     sart_game = True
#     mot_cacher =["*"]*len(mot)
#     print("".join(mot_cacher))
#     nbr_de_chance = 3
#     flag = False
#     cara_t = []
#     mail = input("Entrer votre nom svp : ")
#     progress = [
#        {
#             "email" : mail,
#             "nombre_de_chance" : nbr_de_chance,
#             "level" : {
#                         "mot" : mot,
#                         "mot_trouver" : cara_t
#             }
#        }
#     ]

# drapeau = True

# with open('progress.json', 'r') as a :
#    b = a.read()
#    players = json.loads(b)
#    print(players)
#    for player in players :
#       if player ["email"] == mail :
#          print("vous avez effectivement un progression")
#       else :
#          drapeau = False
#          print("Vous n'avez de progression")

# with open('progress.json','w') as f :
#    for player in players :
#       if drapeau :
#          progress = player
#          print("Vous avez une progression")
#       else :
#          print("Vous n'avez de progression")
#          print("J'ai creer un nouvelle progression")

# while sart_game :
#    caract = input('Entrer un caractere svp : ')
#    if (type(caract) is not str) and (len(caract) != 1) :
#       caract = input('Entrer un caractere svp : ')
#    for i in range(len(mot)) :
#       if mot[i] == caract :
#         mot_cacher[i] = caract
#         flag = True
#    if flag:
#       flag = False
#    else :
#          nbr_de_chance -= 1
#          if nbr_de_chance <= 0 :
#             print("Vous n'avez pas trouvrer le mot ")
#             print("----- VOUS AVEZ PERDU -----")
#             sart_game = False
#          else :
#             print(f"il vous reste {nbr_de_chance} nombre de chance ")
#    ap = "".join(mot_cacher)
#    print(ap)
#    print(f"Les caractères que vous avez trouvez{cara_t}")

#    if ap == mot :
#       sart_game = False

# progress = [
#     {
#         "email" : mail,
#         "nombre_de_chance" : nbr_de_chance,
#         "level" : {
#                     "mot" : mot,
#                     "mot_trouver" : cara_t
#         }
#     }
# ]

# f.write(json.dumps(progress))

# print("".join(mot_cacher))