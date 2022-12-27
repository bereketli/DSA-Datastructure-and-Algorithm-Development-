# Enter your code here. Read input from STDIN. Print output to STDOUT
english_num = int(input())
english = set(input().split(" "))
french_num = int(input())
print(len(english.union(set(input().split(" ")))))