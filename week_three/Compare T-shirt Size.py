compare = int(input())
for i in range(compare):
    two_stri = input().split(" ")
   
    left = len(two_stri[0]) - 1
    right = len(two_stri[1]) - 1
    if two_stri[0] == two_stri[1]:
        print("=")
    elif ord(two_stri[0][left]) < ord(two_stri[1][right]):
        print(">")
    elif ord(two_stri[0][left]) > ord(two_stri[1][right]):
        print("<")
    else:
        
        if two_stri[0][left] == "S":
            if len(two_stri[0]) > len(two_stri[1]):
                print("<")
            else:
                print(">")
            
        else:
            if len(two_stri[0]) > len(two_stri[1]):
                print(">")
            else:
                print("<")
        