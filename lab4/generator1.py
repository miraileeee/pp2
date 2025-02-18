<<<<<<< HEAD
def square(n):
    for i in range (1, n + 1):
        yield i ** 2
    
n = int(input('Number: '))
res = square(n)
for x in res:
=======
def square(n):
    for i in range (1, n + 1):
        yield i ** 2
    
n = int(input('Number: '))
res = square(n)
for x in res:
>>>>>>> e8d0fc96cf3dff340827b2be2b410d75d5e2b020
    print(x)