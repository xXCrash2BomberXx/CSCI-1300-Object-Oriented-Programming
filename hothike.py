days = int(input())
temps = [int(i) for i in input().split()]
sums = []
for i in range(len(temps)-2):
    sums.append(max(temps[i], temps[i+2]))
print(sums.index(min(sums))+1, max(temps[sums.index(min(sums))], temps[sums.index(min(sums))+2]))
