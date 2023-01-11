class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        comment,exprs = "", []
        output = []
        for i in range(len(source)):
            j = 0
            if comment == "" and exprs :
                output.append("".join(exprs))
                exprs = []
                
            while j < len(source[i]):
                if source[i][j : j + 2] == "//" and comment != "/*":
                    if exprs:
                        output.append("".join(exprs))
                        exprs = []
                    break
                elif comment == "" and source[i][j : j + 2] == "/*":
                    comment = "/*"
                    j += 2
                    continue
                elif comment == "/*" and source[i][j : j + 2] == "*/":
                    comment =""
                    j += 2
                    continue
                elif comment =="":
                    exprs.append(source[i][j])
                j += 1
        if comment == "" and exprs :
                output.append("".join(exprs))
                exprs = []
        return output
  
      
        