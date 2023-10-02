class TierNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isWord = False

class Solution:
   
    def inserWord(self, words):  
        for word in words:
            iterator = self.root
            for i in range(len(word)):

                current_char = TierNode()
                if not iterator.children[ord(word[i]) - 97]:
                    iterator.children[ord(word[i]) - 97] = current_char
                 
                iterator = iterator.children[ord(word[i]) - 97]

                if i == len(word) - 1:
                    iterator.isWord = True

                    
    def findWords(self, node, path):
        if not node.isWord:
            return 
        if len(path) > len(self.maxpath):
            self.maxpath = "".join(path)
        
      
        for i in range(26):
            if node.children[i]:
                iterator = node.children[i]
                self.findWords(iterator, path + [chr(97 + i)])
        

    def longestWord(self, words: List[str]) -> str:
       words.sort()
       self.root = TierNode() 
       self.maxpath = ""
       self.root.isWord = True
       self.inserWord(words)
       self.findWords(self.root, [])
       return self.maxpath
