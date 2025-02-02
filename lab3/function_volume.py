def volume(r):
    v = (4/3) * 3.14159265 * r**3
    return v
r = float(input("Radius: "))
v = volume(r)
print("Volume: " + str(round(v, 2)))
