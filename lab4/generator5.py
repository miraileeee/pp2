def reversed(n):
    for i in range(n + 1):
        yield n
        n -= 1
n = int(input('Number: '))
res = reversed(n)
for x in res:
    print(x)