<<<<<<< HEAD
import re

def matchseq(s):
    pattern = 'ab*?'
    if re.search(pattern, s):
        print('Match found')
    else:
        print('Match not found')
    
s = input()
=======
import re

def matchseq(s):
    pattern = 'ab*?'
    if re.search(pattern, s):
        print('Match found')
    else:
        print('Match not found')
    
s = input()
>>>>>>> bd14d7758789e569cd54ee8b28168336f440fff9
matchseq(s)