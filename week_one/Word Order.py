from collections import Counter
def word_order(wordarr):
       count =Counter(wordarr)
       return count
list_word=[]
while True:
    try:
        word =input()  
    except EOFError:
        break
    list_word.append(word)
count = word_order(list_word[1:])
print(len(count)) 
distinct = set()
for word in list_word[1:]:
   if word not in distinct:
      print(count[word],end=" ")
      distinct.add(word)
    
    
# Enter your code here. Read input from STDIN. Print output to STDOUTorder