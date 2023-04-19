#EXO  1 : retourner le mot le plus long d'une phrase
# def longueur(phrase):
#     tableau = phrase.split()
#     premier_mot = tableau[0]
#     for i in tableau:
#         if len(i) > len(premier_mot):
#             premier_mot = i
#     return premier_mot
# print(longueur('hello how are  est un test de la lpart d\'Altesse ? s voir marginalisation'))



# EXO 2 retourne les elements d'un tabbleau dans l'ordre croissant
# def croissant(tableau):
#     for i in range(len(tableau)):
#         for j in range(len(tableau)):
#             if tableau[i] < tableau[j]:
#                 tableau[i] , tableau[j] = tableau[j] , tableau[i]               
#     print(tableau)
# croissant([2,3,9,9,-2])



# EXO 3  retounrner le nmbre de % d'une lettre qu'il ya dans un mot (frequence)
# def frequence(a):
#     diction = {}
#     for i in a:
#         trie = a.count(i)
#         diction[i] = f"{round((100*trie)/len(a))}%"
#     return diction
# print(frequence("je suis en classe"))


#EXO 4  retourner si le mot est dans l'autre (anagramme)
def anagramme(mot1,mot2):
    if type(mot1) and type(mot2) is str:
        for i in mot2 :
            if i not in mot1:
                return "Pas anagramme"
        return "anagramme"
    return -1
print(anagramme("bonjour","hello"))


#EXO 5 
    

