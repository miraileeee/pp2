<<<<<<< HEAD
import re
def snaketocamel(s):
    res = re.sub('_(.)', lambda up: up.group(1).upper(), s)  #group inside (.)
    camel = res[0].lower() + res[1:]
    print(camel)

s = input()
snaketocamel(s)
=======
import re
def snaketocamel(s):
    res = re.sub('_(.)', lambda up: up.group(1).upper(), s)  #group inside (.)
    camel = res[0].lower() + res[1:]
    print(camel)

s = input()
snaketocamel(s)
>>>>>>> bd14d7758789e569cd54ee8b28168336f440fff9
    