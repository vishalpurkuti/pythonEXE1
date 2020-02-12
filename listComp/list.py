sqr = []
for x in range(5):
    sqr.append(x**2)
print(sqr)


cubes = list(map(lambda x: x*3, range(5)))
print(cubes)

cubes2 = [x**3 for x in range(10)]
print(cubes2)
