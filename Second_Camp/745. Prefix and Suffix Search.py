class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1

class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()

        for idx, word in enumerate(words):
            for i in range(len(word) + 1):
                for j in range(len(word) + 1):
                    self.insert(word[i:] + "#" + word[:j], idx)

    def insert(self, word, idx):
        current = self.root
        current.index = idx

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.index = idx

    def f(self, prefix: str, suffix: str) -> int:
        search_word = suffix + "#" + prefix
        current = self.root

        for char in search_word:
            if char not in current.children:
                return -1
            current = current.children[char]

        return current.index
