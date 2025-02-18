<<<<<<< HEAD
def reversed(n):
    for i in range(n + 1):
        yield n
        n -= 1
n = int(input('Number: '))
res = reversed(n)
for x in res:
=======
def reversed(n):
    for i in range(n + 1):
        yield n
        n -= 1
n = int(input('Number: '))
res = reversed(n)
for x in res:
>>>>>>> e8d0fc96cf3dff340827b2be2b410d75d5e2b020
    print(x)