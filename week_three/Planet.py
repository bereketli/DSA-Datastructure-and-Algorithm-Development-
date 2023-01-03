from collections import Counter
no_test = int(input())
for i in range(no_test):
    cost_two = int(input().split(" ")[1])
    count = Counter(input().split(" "))
    cost_total = 0
    for key in count:
        if count[key] >= cost_two:
            cost_total += cost_two
        else:
            cost_total += count[key]
    print(cost_total)