class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        current = ""
        for char in path:
            
            if char == "/":
                if stack and current == "..":
                    stack .pop()
                elif current and current != ".." and current != ".":
                    stack.append(current)
                current = ""
            else:
                current += char
        if stack and current == "..":
            stack.pop()
        elif current and current != ".." and current != ".":
            stack.append(current)

        
        return "/" + "/".join(stack)
                    
            
       
