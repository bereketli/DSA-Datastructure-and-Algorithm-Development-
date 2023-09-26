class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        iterator = self.root
        for i in range(len(word)):
            if not iterator.children[ord(word[i]) - ord('a')]:
                iterator.children[ord(word[i]) - ord('a')] = TrieNode()
            iterator = iterator.children[ord(word[i]) - ord('a')]
        iterator.isWord = True

    def search(self, word: str) -> bool:
        def backtrack(node, idx):
            if idx == len(word):
                return node.isWord
            char = word[idx]
            if char == '.':
                for child in node.children:
                    if child and backtrack(child, idx + 1):
                        return True
            else:
                child = node.children[ord(char) - ord('a')]
                if child:
                    return backtrack(child, idx + 1)
            return False

        return backtrack(self.root, 0)
