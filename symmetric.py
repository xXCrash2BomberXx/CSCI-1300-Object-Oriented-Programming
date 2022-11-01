array = []
t = None
while t != 0:
    t = int(input())
    if t != 0:
        array.append([])
        for i in range(t):
            array[-1].append(input())

for i in range(len(array)):
    print("SET", i+1)
    for t in range(0, len(array[i]), 2):
        print(array[i][t])
    for t in range(len(array[i])-(2 if len(array[i])%2 != 0 else 1), 0, -2):
        print(array[i][t])
