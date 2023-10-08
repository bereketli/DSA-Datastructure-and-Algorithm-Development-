t = int(input())
for _ in range(t):
    n = int(input())
    sequence = list(map(int, input().split()))
    total_sum = 0
    current_max = sequence[0]
    is_positive = current_max > 0 
    for num in sequence:
        
        if is_positive == (num > 0):
            current_max = max(current_max, num)
            
          
        else:
           
            total_sum += current_max
            current_max = num 
            is_positive = num > 0     

    total_sum += current_max
    print(total_sum)

