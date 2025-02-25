import re
def colon(s):
    res = re.sub('[,. ]', ';', s)
    print(res)
s = input()
colon(s)