class Solution(object):
    def partitionLabels(self, s):
       dic ={}
       for i in range(len(s)):
            dic[s[i] ] =i
       count ,output=0, []
       maxi =0
       for i in range(len(s)):
            maxi = max(maxi, dic[s[i]])
            count +=1
            if i == maxi:
                output.append(count)
                count =0
       return output
                
                
       