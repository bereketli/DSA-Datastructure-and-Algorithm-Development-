m, n = map(int, input().split())
firstnum = list(map(int, input().split()))
secondnum = list(map(int, input().split()))
merged = []
first_point = 0
second_point = 0
while first_point < m and second_point < n:
    if firstnum[first_point] <= secondnum[second_point]:
        merged.append(firstnum[first_point])
        first_point += 1
    else:
        merged.append(secondnum[second_point])
        second_point += 1
merged.extend(firstnum[first_point:])
merged.extend(secondnum[second_point:])
print(* merged)
