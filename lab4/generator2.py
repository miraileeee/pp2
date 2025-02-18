<<<<<<< HEAD
def even(n):
    for i in range (2, n + 1, 2):
        yield i
n = int(input('Number: '))
res = even(n)
=======
def even(n):
    for i in range (2, n + 1, 2):
        yield i
n = int(input('Number: '))
res = even(n)
>>>>>>> e8d0fc96cf3dff340827b2be2b410d75d5e2b020
print(', '.join(str(x) for x in res))