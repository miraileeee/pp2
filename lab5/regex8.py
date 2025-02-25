import re

def splitup(s):
    res = re.split('(?=[A-Z])', s)
    print(res)

s = input()
splitup(s)