class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_int = []
        for i in range(len(words)):
            int_word = 0
            distinct = set()
            for letter in words[i]:
                if letter not in distinct:
                    int_word += 2** (ord(letter) - 97)
                    distinct.add(letter)
            words_int.append(int_word)
        
        max_product = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words_int[i] & words_int[j] == 0:
                    max_product = max(max_product, len(words[i]) *len(words[j] ) )
        return max_product
                   
