# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
size = input().split(" ")
count =  defaultdict(list)
for i in range(int(size[0])):
    count[input()].append(str(i + 1))
    
for i in  range(int(size[1])):
    b = input()
    output= " ".join(count[b]) if count[b] != [] else -1
    print (output)