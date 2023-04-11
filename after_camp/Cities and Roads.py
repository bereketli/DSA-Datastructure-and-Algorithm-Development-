n = int(input())
count_road = 0
for i in range(n):
    ithroads = list(map(int, input().split()))
    for road in range(i + 1, n):
        if ithroads[road] != 0:
            count_road += 1
print(count_road)
