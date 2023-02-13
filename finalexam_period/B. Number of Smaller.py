size =[int(num) for num in input().split(" ")]
first = [int(num) for num in input().split(" ")]
second = [int(num) for num in input().split(" ")]
firstP = 0 
output = []
for secondP in range(size[1]):
    while firstP < size[0] and first[firstP] < second[secondP]:
        firstP += 1
 
    output.append(firstP)
print(*output)