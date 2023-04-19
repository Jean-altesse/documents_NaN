#Un tableau qui nous return la table de multiplication et les virgules

def multi (nbr):
    if type(nbr) is int:
        tab = []
        for i in range (1,11) :
            tab.append(str(nbr*i))
        result = ",".join(tab[0:6]) + ",...," + str(tab[-1])
        return result
    
print(multi(5))

#Apprendre les Tableaux