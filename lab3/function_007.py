def spy_game(nums):
    spy = [0, 0, 7]
    i = 0
    for x in nums:
        if x == spy[i]:
            i += 1
        if i == len(spy):
            return True
    return False

nums = list(map(int, input()))
if spy_game(nums):
    print("True")
else:
    print("False")