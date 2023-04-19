# def fib(n:int) -> int:
#     if n <= 2:
#         return 1
#     return fib(n-1)+fib(n-2)
# print(fib(5))


#  fontion qui return la suite d'une suie :

def U(n:int) -> int:
    if n <= 2:
        return 1
    return 3*U(n-1) + U(n-2)
print(U(6))