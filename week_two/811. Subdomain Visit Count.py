take = int(input())
for m in range(take):
    stri = input().split(" ")
    output= ["abebe"] * len(stri)
   
    
    for i in range(len(stri)):
        j = 0
        while j < len(stri[i]):
            index =""
            flag = False
            
            while  j < len(stri[i]) and stri[i][j].isnumeric():
                
                index += stri[i][j] 
                
                flag = True
                j +=1
          
            if flag :
               
                fin =stri[i][j :] if j < len(stri[i])  else ""
               
                
                output[int(index)  -1] = stri[i][:j - len(index)] + fin
                break
            j +=1
    print(" ".join(output))

    