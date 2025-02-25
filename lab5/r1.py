import re
def matchseq(s):
    pattern = 'ab*?'
    if re.search(pattern, s):
        print('Match found')
    else:
        print('Match not found')
s = input()
matchseq(s)