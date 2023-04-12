class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        removed = {}
        last_index = {}
        stack = []
        # register the last index of each character 
        for i in range(len(s)):
            last_index[s[i]] = i
            removed[s[i]] = True
        
        for i in range(len(s)):
            if removed[s[i]]:
                while stack and s[stack[-1]] > s[i] and i < last_index[s[stack[-1]]]:
                    popped = stack.pop()
                    removed[s[popped]] = True
                stack.append(i)
                removed[s[i]] = False
        stack = [s[i] for i in stack]
        return "".join(stack)
                
       
        """
        last_index  to register the last index of each character
        removed   to chack if the element is already added to the stack
        increasing monotonic stack     to make the string lexicographically smaller
        """
