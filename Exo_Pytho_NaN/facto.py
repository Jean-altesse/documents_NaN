# def facto(a) :
#   if a < 0 or a > 15 :
#       return -1
#   else :
#       fact = 1
#       cal = 1
#       while cal < a :
#           fact = fact * (cal+1)
#           cal = cal + 1
#       return fact
    
# print(facto(5))


#   Fonction recussive de fatoriel :
# def factoriel(n:int)-> int:
#     if not isinstance(n,(int)) or n < 0:
#         return -1
#     if n == 0:
#         return 1
#     return n * factoriel (n -1)
# print(factoriel(5))

def factoriel(n:int)-> int:
    if not isinstance(n,(int)) or n < 0:
        return -1
    if n == 0:
        return 1
    print(n**2)
    return n**2 + factoriel (n -1)
print(factoriel(5))