val = None
sol = []
while val != 0:
    val = int(input())
    if val != 0:
        test = 11
        while True:
            if sum([int(char) for char in str(val*test)]) == sum([int(char) for char in str(val)]):
                sol.append(test)
                break
            else:
                test += 1
for i in sol:
    print(i)