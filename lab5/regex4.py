import re

def up1_low1(s):
    pattern = '^[A-Z]+[a-z]*'
    if re.search(pattern, s):
        print('Match found')
    else:
        print('Match not found')
    
s = input()
up1_low1(s)