<<<<<<< HEAD
def divby3and4(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
        
n = int(input('Number: '))
res = divby3and4(n)
for x in res:
=======
def divby3and4(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
        
n = int(input('Number: '))
res = divby3and4(n)
for x in res:
>>>>>>> e8d0fc96cf3dff340827b2be2b410d75d5e2b020
    print(x)