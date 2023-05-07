test = int(input())
for _ in range(test):
    a, b = list(map(int, input().split()))
    print(min(min(a,b), ((a + b) // 4)))
