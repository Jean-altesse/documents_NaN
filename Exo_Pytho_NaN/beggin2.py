
#  --------------------JEUX de Combat-------------------
'''class Player :
   def __init__(self,nom,point_de_vie,point_dattaque,arme,altesse) :
      if type(nom) is not str :
        raise TypeError ("le nom n'est pas une chaine de caractère")
      if type(point_de_vie) is not int :
         raise TypeError ("le point de vie doit être un entier")
      if type (point_dattaque) is not int :
         raise TypeError ("le point d'attaque doit être un entier")
      if type(arme) is not Weapon :
         raise TypeError ("Votre arme doit être une chiane de caractere")
      self.nom=nom
      self.point_de_vie=point_de_vie
      self.point_dattaque=point_dattaque
      self.arme=arme
      self.altesse=altesse

   def face_to_face(self,player2) :
       print(f"j'attaque joeur 2 {player2.nom}")
       if self.point_dattaque > player2.point_dattaque :
          player2.point_de_vie -= 1
          return f"le joueur 2 {player2.nom} et blesser , sa vie diminue {player2.point_de_vie}"
       elif self.point_dattaque < player2.point_dattaque :
          self.point_de_vie -= 1
          return f"le joueur {self.nom} a perdu , sa vie a diminuée {player2.point_de_vie}"
       else :
          return f"nous avons le même point d'attaque"

   def __repr__(self) :
      print("votre nom est :",self.nom)
      print("votre ponit d'attaque est de :",self.point_dattaque)
      print("votre point de vie est de :",self.point_de_vie)

   def attaquer (self,player) :
      if self.arme.tipe == "rapprocher" :
          self.face_to_face()
      elif self.arme.tipe == "distant" :
         player.point_de_vie = player.point_de_vie - self.arme.deguard
      else:
         raise NameError ("Votre arme n'est pas reconnue") 
      

class Weapon :
  def __init__(self ,nom ,deguard,tipe) :
      self.nom = nom
      self.deguard= deguard
      self.tipe = tipe

  def presente_arme (self) :
      print ("votre arme sappelle : ", self.nom)
      print ("vous avez un degard de : " , self.deguard)
      print ("vous arme est de type")


    

  
   # def defense(self , joueur) :
    #   if joueur.point_dattaque > self.point_dattaque :
     #     self.point_de_vie -= 1
      #    print(f"{}")
  '''




   











    
 

        
        
    

