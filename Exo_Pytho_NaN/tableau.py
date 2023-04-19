
# class Array:
#    tab = []
#    def __init__(self,*args):
#         self.tab=list(args)
#         print(args)
        
#         pass
    
#    def lenght (self):
#          cpt = 0
#          for i in self.tab:
#             cpt += 1
#          return cpt
   
#    def filter  (self , callback):
#        b = []
#        for i in self.tab:
#            if callback (i):
#                a.append(i)

#                return a       

# a = Array(1,3,8,9,7,7)




#    tab=[]
#     for i in range (1,1000):
#        if nbrpremier(i):
#            tab.append(i)
#    print(i)


import random 

tab = ["vallecano","bordeaux","empoli","torino","apoel",
       "las palmas","nottingham","aston villa",
       "mamelodi","inter milan","young boys",
       "dortmund","barcelone","panathinaikos",
       "toulous","celta vigo","burnley","swansea",
       "sanderland","exerter","lincoln","milton keynes",
       "newport","mansfield","queen's park","tenerif",
       "red star","dunkerque","chateauraux"
       ]

print(random.choice(tab))