def palind(s):
    rev = s[::-1]
    if rev == s:
        print("Palindrome")
    else:
        print("Not a palindrome")
    
s = input()
s = s.lower()
palind(s)