def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
    
a = int(input('Number 1:'))
b = int(input('Number 2:'))
res = squares(a, b)
for x in res:
    print(x)