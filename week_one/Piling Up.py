# Enter your code here. Read input from STDIN. Print output to STDOUT
num_testcase = int(input())
for i in range(num_testcase):
    n = int(input())
    cubes = [int(value) for value in input().split(" ")]
    left , right= 0, n -1
    bottom = float("inf")
    while left < right and bottom >= max(cubes[right],cubes[left]):
        if cubes[right] >= cubes[left]:
            bottom = cubes[right]
            right -=1
        else:
            bottom = cubes[left]
            left +=1
            
    if left == right :
        print ("Yes")
    else:
        print("No")
        