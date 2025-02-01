def is_prime(num):
    if num > 1:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True
    else: 
        return False
    
def filter_prime(melist):
    res = []
    for num in melist:
        if is_prime(num):
            res.append(num)
    return res

inp = input().split()     #to input a list
melist = [int(num) for num in inp]
result = filter_prime(melist)
print(result)