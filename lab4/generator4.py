<<<<<<< HEAD
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
    
a = int(input('Number 1:'))
b = int(input('Number 2:'))
res = squares(a, b)
for x in res:
=======
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
    
a = int(input('Number 1:'))
b = int(input('Number 2:'))
res = squares(a, b)
for x in res:
>>>>>>> e8d0fc96cf3dff340827b2be2b410d75d5e2b020
    print(x)