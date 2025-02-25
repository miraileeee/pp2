import re

def plusspace(s):
    res = re.sub('([a-z])([A-Z])', lambda a: a.group(1) + ' ' + a.group(2), s)
    print(res)

s = input()
plusspace(s)