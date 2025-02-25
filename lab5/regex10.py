import re
def cameltosnake(s):
    res = re.sub('([a-z])([A-Z])', lambda a: a.group(1) + '_' + a.group(2).lower(), s)
    print(res)

s = input()
cameltosnake(s)