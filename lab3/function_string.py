def permute(s):
    if len(s) <= 1:
        return [s]
    str_perm = []
    
    for i in range(len(s)):
        ch= s[i]
        rest = s[:i] + s[i + 1:]
        for perm in permute(rest):
            str_perm.append(ch + perm)
    return str_perm
def print_func():
    s = input()
    str_perm = permute(s)
    for perm in str_perm:
        print(perm)
    
print_func()
