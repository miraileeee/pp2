<<<<<<< HEAD
import re

def up1_low1(s):
    pattern = '^[A-Z]+[a-z]*'
    if re.search(pattern, s):
        print('Match found')
    else:
        print('Match not found')
    
s = input()
=======
import re

def up1_low1(s):
    pattern = '^[A-Z]+[a-z]*'
    if re.search(pattern, s):
        print('Match found')
    else:
        print('Match not found')
    
s = input()
>>>>>>> bd14d7758789e569cd54ee8b28168336f440fff9
up1_low1(s)