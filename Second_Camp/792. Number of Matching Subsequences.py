class Solution:
    class TrieNode:
        def __init__(self):
            self.child = [None] * 26
            self.end_count = 0
            self.isEnd = False

    def insert(self, node, word):
        for char in word:
            index = ord(char) - ord('a')
            if node.child[index] is None:
                node.child[index] = self.TrieNode()
            node = node.child[index]
        node.isEnd = True
        node.end_count += 1

    def findIndex(self, s, c, index):
        for i in range(index, len(s)):
            if s[i] == c:
                return i
        return -1

    def solve(self, s, node, last_index):
        if node.isEnd:
            self.ans += node.end_count
        for i in range(26):
            if node.child[i] is not None:
                c = chr(i + ord('a'))
                new_index = self.findIndex(s, c, last_index + 1)
                if new_index != -1:
                    self.solve(s, node.child[i], new_index)

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        self.ans = 0
        self.root = self.TrieNode()
        for word in words:
            self.insert(self.root, word)
        temp = self.root
        self.solve(s, temp, -1)
        return self.ans

        


        
