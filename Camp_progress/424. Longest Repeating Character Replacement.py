class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        stack = deque()
        count_window = {}
        maxsize = left = sum_char= 0

        # decreasing mono que to get the most repeating character
        def monostack (num):
            while stack and stack[-1] < num:
                stack.pop() 
            stack.append(num)
        
        for right in range(len(s)):
            if s[right] not in count_window:
                count_window[s[right]] = 1
            else:
                count_window[s[right]] += 1
            monostack(count_window[s[right]])
            sum_char += 1
            
            while stack and sum_char - stack[0] > k:
               
                if count_window[s[left]] == stack [0]:
                    stack.popleft()
                    monostack(count_window[s[left]] -1)
                count_window[s[left]] -= 1
                left += 1
                sum_char -= 1
            maxsize = max(maxsize, right - left + 1)
        return maxsize

               

        
    
       


