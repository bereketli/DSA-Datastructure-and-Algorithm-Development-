# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
k = int(input())
room_no = list(input().split(" "))

count = Counter(room_no)

for key in count:
    
    if count[key] != k:
        print (key)
        break
