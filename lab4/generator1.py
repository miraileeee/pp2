def square(n):
    for i in range (1, n + 1):
        yield i ** 2
    
n = int(input('Number: '))
res = square(n)
for x in res:
    print(x)