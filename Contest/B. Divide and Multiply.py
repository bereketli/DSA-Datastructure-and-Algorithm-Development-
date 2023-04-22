test = int(input())
for _ in  range(test):
    n = int(input())
    nums = list(map(int, input().split()))
    maxofall = 0
    
    maxnum = [0, 0]
    
    for j, value in enumerate(nums):
        maxnum = [j, value ]
        nums_cp = nums.copy()
        for i in range(len(nums)):

            while maxnum[0] != i and nums_cp[i] % 2 == 0:
                maxnum[1] *= 2
                nums_cp[i] /= 2 
        nums_cp[maxnum[0]] = maxnum[1]
        maxofall = int(max(maxofall, sum(nums_cp)))
    print(maxofall)
    
