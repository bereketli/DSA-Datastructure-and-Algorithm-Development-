test = int(input())
for test_cases in range(test):
    num = int(input())
    if num == 1:
         print(3)
         continue
    num_bin = list(bin(num))
   
    soln = ["0", "b"] + (["0"] *(len(num_bin) - 2))
    point_num = len(num_bin) - 1
    and_idx = None

    #finding a y and Y & x > 0
    while num_bin[point_num] != "b":
            if num_bin[point_num] == "1":
                 soln[point_num] = "1"
                 and_idx = point_num
                 break
            point_num -= 1
            
    #finding a y and Y ^ x > 0
    if num_bin == soln:
        point_num = len(num_bin) - 1
        while soln[point_num] != "b":
            if point_num == and_idx:
                point_num  -= 1
                continue

            if num_bin[point_num] == soln[point_num]:
                soln[point_num] = str(abs(int(soln[point_num] ) - 1))
                break
            point_num -= 1
            
    print(int("".join(soln), 2))

          
