import json

#Creer une base de données avec json quo demandde a l'utilisateur de s'inscrire ou se connecter et apres verifier dans la bases de données

print("Bonjour bienvenue etranger")
verif = input ("Entrer 1 pour se Connecter ou Entrer 2 pour s'inscrire")

if verif == "1" :

    mail = input("Entrer votre mail svp : ")
    passw = input("Entrer votre mot de pass svp : ")

    stk = {mail : passw}
    while open("connexion.json","a") :
        json.dump(stk , indent=10)

elif verif == "2" :

    mail = input("Entrer votre mail svp : ")
    passw = input("Entrer votre mot de pass svp : ")

    stk = {mail : passw}
    while open("inscrire.json","a") :
        json.dump(stk , indent=10)

else :
    print("Vous entrer 1 ou 2 ")



