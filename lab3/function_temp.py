def temp_func(faren):
    centi = (5 / 9) * (faren - 32)
    return centi
faren = int(input())
centi = temp_func()
print(str(faren) + " farenheit is " + str(round(centi, 4)) + " celcius")