import re

def anotb(s):
    pattern = '^a.*b$'
    if re.search(pattern, s):
        print('Match found')
    else:
        print('Match not found')
    
s = input()
anotb(s)