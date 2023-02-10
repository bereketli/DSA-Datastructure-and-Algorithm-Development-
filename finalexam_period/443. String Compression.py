class Solution:
    def compress(self, chars: List[str]) -> int:
        left,count=0,0
        for right in range(len(chars)):
           
            if chars[left]==chars[right]:
                count+=1
            else:
                left+=1
                if count==1:
                    chars[left]=chars[right]
                    continue
                else:
                    for char in str(count):
                        chars[left]=char
                        left+=1
                    count=1
                    chars[left]=chars[right]
        if count>1:
          for char in str(count):
                 left+=1
                 chars[left]=char
                       
        
        return left+1