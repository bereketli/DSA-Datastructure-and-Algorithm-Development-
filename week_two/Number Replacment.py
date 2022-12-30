testcase = int(input())
for i in range(testcase):
    flag = False
    count = {}
    n = int ( input())
    number = input().split(" ")
    compare = input()
    for j in range(len(number)):
        if number[j] not in count:
            count[number[j]] = set(compare[j])
        else:
            count[number[j]].add(compare[j])
    for cou in count:
       if len(count[cou]) > 1:
           print("No")
           flag = True
           break
    if not flag:
       print("YES")
           
           
            