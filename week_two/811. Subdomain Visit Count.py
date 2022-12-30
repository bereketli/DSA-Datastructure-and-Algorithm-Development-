class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count, output= {}, []
        for string in cpdomains:
            splited = string.split(" ")
           
            num = int(splited[0])
         
            for j in range(len(splited[1])):
                if j == 0 or splited[1][j] == ".":
                    first = j if j == 0 else j + 1
                    if splited[1][first:] not in count:
                        count[splited[1][first: ]] = num
                    else:
                        count[splited[1][first: ]] += num
        for domain in count:
            final = (str(count[domain]) + " " +domain)  
            output.append(final)
        return output


