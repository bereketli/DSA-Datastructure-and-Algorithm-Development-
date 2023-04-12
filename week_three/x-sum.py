test = int(input())
for _ in range(test):
    n, m = map(int, input().split())
    taken2d = []
    # accepting inputs
    for i in range(n):
        taken2d.append(list(map(int, input().split())))
    
    upsum, downsum={},{}
    # upsum
    for i in range(n):
        row = i
        column, sum= 0, 0
        while row >= 0 and column < m:
            
            sum += taken2d[row][column]
            row -= 1
            column += 1
        upsum[column + row] = sum
    for i in range(m):
        row = n - 1
        column , sum = i, 0
        while column < m and row >= 0:
            sum += taken2d[row][column]
            row -= 1
            column += 1
        upsum[column + row] = sum
        
 
    # downsum 
    for i in range(m - 1, -1, -1):
        row = 0
        column, sum = i, 0
        while column < m  and row < n:
            sum += taken2d[row][column]
            row += 1
            column += 1
        downsum[column - row] = sum
    for i in range( n):
        row = i
        column, sum = 0, 0
        while row < n and column < m:
            sum += taken2d[row][column]
            row += 1
            column += 1
        downsum[column - row] = sum
    
    # main 
    maxsum = 0
    for i in range(n):
         for j in range(m):
          
            maxsum = max(maxsum, downsum[j - i] + upsum[ j + i] - taken2d[i][j])
            
    print(maxsum)
