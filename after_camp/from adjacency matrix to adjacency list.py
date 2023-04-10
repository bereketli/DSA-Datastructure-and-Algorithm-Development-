n = int(input())
for i in range(n):
    itmatrix = list(map(int, input().split()))
    adjecent = []
    for j in range(len(itmatrix)):
        if itmatrix[j] != 0:
            adjecent.append(j + 1)
    print(len(adjecent), * adjecent)
