def ounces_func(grams):
    ounces = 28.3495231 * float(grams)
    return ounces
grams = input()
ounces = ounces_func()
print(str(grams) + " grams is " + str(round(ounces,7)) + " ounces")
    