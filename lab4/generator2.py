def even(n):
    for i in range (2, n + 1, 2):
        yield i
n = int(input('Number: '))
res = even(n)
print(', '.join(str(x) for x in res))