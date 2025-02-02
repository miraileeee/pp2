def reverse_words():
    s = input()
    words = s.split()
    reversed = []
    for i in words:
        reversed.insert(0, i)
    
    return reversed
reversed = reverse_words()
print(" ".join(reversed))