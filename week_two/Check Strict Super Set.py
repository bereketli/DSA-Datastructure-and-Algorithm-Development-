# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split(" "))
n = int(input())
flag = True
for i in range(n):
    newset = set(input().split(" "))
    if len(A) <= len(newset) or not A.issuperset(newset):
        print(False)
        flag = False
        break
if flag:
    print(True)
    