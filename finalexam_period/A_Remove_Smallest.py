testcase = int(input())
for _ in range(testcase):
    size = int(input())
    arr = list(map(int, input().split()))
    count_removed = 0
    arr.sort()
    for i in range(1, size):
        if arr[i -1 ] == arr[i] or (arr[i - 1] +1 == arr[i]):
            arr[i-1] = " "
            count_removed += 1
        
            
    if count_removed == size - 1:
        print("YES")
    else:
        print("NO")
