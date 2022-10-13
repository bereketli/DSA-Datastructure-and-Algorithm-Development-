class Solution(object):
    def topKFrequent(self, words, k):
        count ={}
        for i in range(len(words)):
            if words[i] not in count:
                count[words[i]] =1
            else:
                count[words[i]] +=1
        sorted_word=sorted(count.items(), key=lambda kv:(kv[1],kv[0]))
        output=[]
        for i in range(len(sorted_word) -1, -1 ,-1):
                output.append(sorted_word[i][0])
        
       
        for i in range(len(output)):
            
            for j in range(i + 1,len(output)):
                if count[output[i]] == count[output[j]] and output[i] >output[j]:
                    output[i], output[j]=output[j], output[i]
       
        return output[0: k]
                    
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        