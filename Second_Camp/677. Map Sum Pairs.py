class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False
        self.prefixSum = 0
      


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.current_value = {}      

    def insert(self, key: str, val: int) -> None:
        temp = self.root
        if key in self.current_value:
            self.similarHandler(key, val)
            
        else:
            self.uniqueHandler(key, val)
        
        self.current_value[key] = val


    def uniqueHandler(self, key, val):
        print(key)
     
        temp = self.root

        for char in key:
            if not temp.children[ord(char) - ord("a")]:
                temp.children[ord(char) - ord("a")] = TrieNode()
            temp = temp.children[ord(char) - ord("a")]
            temp.prefixSum += val
        
        temp.isWord = True

    def similarHandler(self, key, val):

        temp = self.root
        for char in key:
            
            temp = temp.children[ord(char) - ord("a")]
            temp.prefixSum += (val - self.current_value[key])
            
        temp.isWord = True


    def sum(self, prefix: str) -> int:
        temp = self.root
        
        for char in prefix:
            print(char)
            if temp.children[ord(char) - ord("a")]:
                temp = temp.children[ord(char) - ord("a")]
            else:
                return 0
        return temp.prefixSum

        
