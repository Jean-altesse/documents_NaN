import random


nbr_mystere = random.randint(1,100)
chance = 10
while chance > 0 :
    nombre = int(input("Entrer un nombre compris entre 1 et  0100 :"))
    if nombre == nbr_mystere:
        print(f'Vous avez trouvez juste le nombre mystere etais {nbr_mystere}')

    else:
        chance -= 1
        if chance <= 0 :
                print("Vous avez ecoulez vos chances")
                print(f"Le chiffre etais {nbr_mystere}")
        elif nombre > nbr_mystere:
                print("c'est moins")
                print(f"Il vous reste {chance} veillez reessayer")
        elif nombre < nbr_mystere:
                print("c'est plus")
                print(f"Il vous reste {chance} veillez reessayer")
        else:
                print(f"Il vous reste {chance} veillez reessayer")