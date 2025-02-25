import re
def snaketocamel(s):
    res = re.sub('_(.)', lambda up: up.group(1).upper(), s)  #group inside (.)
    camel = res[0].lower() + res[1:]
    print(camel)
s = input()
snaketocamel(s)