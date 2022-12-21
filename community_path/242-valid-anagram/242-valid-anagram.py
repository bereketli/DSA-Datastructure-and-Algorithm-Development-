class Solution(object):
    def isAnagram(self, s, t):
        if len(t)!=len(s):
            return False
        else:
            dictionarys={}
            dictionaryt={}
            for ins in s:
                if (ins in dictionarys):
                    dictionarys[ins]+=1
                else: dictionarys[ins]=1
            for chilt in t:
                  if (chilt in dictionaryt):
                    dictionaryt[chilt]+=1
                  else: dictionaryt[chilt]=1
            return True  if(dictionarys==dictionaryt) else False
               
            
                
                
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        