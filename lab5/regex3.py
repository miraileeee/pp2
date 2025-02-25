import re

def matchunder(s):
    pattern = '^[a-z]+_[a-z]+$'
    if re.search(pattern, s):
        print('Match found')
    else:
        print('Match not found')
    
s = input()
matchunder(s)