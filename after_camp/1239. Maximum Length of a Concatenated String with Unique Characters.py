class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.max_length = 0
        self.backtrack(arr, "", 0)
        return self.max_length

    def backtrack(self, arr, current, start):
        if self.max_length < len(current):
            self.max_length = len(current)
        
        for i in range(start, len(arr)):
            if not self.is_valid(current, arr[i]):
                continue
            self.backtrack(arr, current + arr[i], i + 1)

    def is_valid(self, current_string, new_string):
        char_count = [0] * 26
        for char in new_string:
            index = ord(char) - ord('a')
            char_count[index] += 1
            if char_count[index] == 2:
                return False
            
            if char in current_string:
                return False
        
        return True
        
