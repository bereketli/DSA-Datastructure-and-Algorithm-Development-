n= input()
arr1 = list(input().split(" "))
int_arr1 = [int(arr) for arr in arr1]
seta = list(input().split(" "))
int_seta = set([int(a) for a in seta if a.isalnum()])
setb = list(input().split(" "))
int_setb = set([int(b) for b in setb if b.isalnum()])
solution = 0
for arr in int_arr1:
    if arr in int_seta:
        solution +=1
    if arr in int_setb:
        solution -=1
   
print(solution)
