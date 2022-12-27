# Enter your code here. Read input from STDIN. Print output to STDOUT
no_english = int(input())
english = set(input().split(" "))
no_french = int(input())
french = set(input().split(" "))
no_only_eng = english.difference(french)
print( len(no_only_eng))