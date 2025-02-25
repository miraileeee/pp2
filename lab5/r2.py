import re
def matchseq(s):
    pattern = 'ab{2,3}'
    if re.search(pattern, s):
        print('Match found')
    else:
        print('Match not found')
s = input()
matchseq(s)