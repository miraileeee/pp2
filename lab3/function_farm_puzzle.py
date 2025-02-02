def farm_func(heads, legs):
    rabs = (legs - 2 * heads) / 2
    chicks = heads - rabs
    if rabs == int(rabs) and chicks == int(chicks):
        return int(rabs), int(chicks)
    

heads = int(input("Number of heads: "))
legs = int(input("Number of legs: "))
result = (farm_func(heads, legs))
print("Rabbits: " + str(result[0]) + ". Chickens: " + str(result[1]))