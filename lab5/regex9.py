<<<<<<< HEAD
import re

def plusspace(s):
    res = re.sub('([a-z])([A-Z])', lambda a: a.group(1) + ' ' + a.group(2), s)
    print(res)

s = input()
=======
import re

def plusspace(s):
    res = re.sub('([a-z])([A-Z])', lambda a: a.group(1) + ' ' + a.group(2), s)
    print(res)

s = input()
>>>>>>> bd14d7758789e569cd54ee8b28168336f440fff9
plusspace(s)