def unique(inp):
    melist = []
    for item in inp:
        if item not in melist:
            melist.append(item)
    return melist
inp = input()
melist = unique(inp)
print(melist)