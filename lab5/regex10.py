<<<<<<< HEAD
import re
def cameltosnake(s):
    res = re.sub('([a-z])([A-Z])', lambda a: a.group(1) + '_' + a.group(2).lower(), s)
    print(res)

s = input()
=======
import re
def cameltosnake(s):
    res = re.sub('([a-z])([A-Z])', lambda a: a.group(1) + '_' + a.group(2).lower(), s)
    print(res)

s = input()
>>>>>>> bd14d7758789e569cd54ee8b28168336f440fff9
cameltosnake(s)