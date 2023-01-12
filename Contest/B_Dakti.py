no_testcase = int(input())
for i in range(no_testcase ):
    keystore ={}
    words = input().split(" ")
   
    for word in words:
        character, num ,j = [] , 0, 0
        while j < len(word):
        
            while j < len(word) and word[j].isdigit() :
                num = num *10 + int(word[j])
                j += 1
            if j < len(word):
                character.append(word[j])
            j +=1
        keystore[num] = "".join(character)
    keystore_orderd= sorted(keystore.keys())

    arranged =[]
    for key in keystore_orderd:
        arranged.append(keystore[key])
    print(" ".join(arranged))
        

