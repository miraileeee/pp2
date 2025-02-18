def divby3and4(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
        
n = int(input('Number: '))
res = divby3and4(n)
for x in res:
    print(x)