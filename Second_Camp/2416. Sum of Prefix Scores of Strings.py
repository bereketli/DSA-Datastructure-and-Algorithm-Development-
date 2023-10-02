class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.count_prefix = 0
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        self.root = TrieNode()
        answer = []
        for word in words:
            self.insert(word)
        
        for word in words:
            answer.append(self.findPrefixes(word))
        
        return answer
   
    def insert(self, word):
        iterator = self.root

        for char in word:
            
            if not iterator.children[ord(char) - ord("a")]:
                iterator.children[ord(char) - ord("a")] = TrieNode()

            iterator = iterator.children[ord(char) - ord("a")]
            iterator.count_prefix += 1
        
    def findPrefixes(self, word):
        iterator= self.root
        count = 0

        for char in word:
            iterator = iterator.children[ord(char) - ord("a")]
            count += iterator.count_prefix
        return count









        
