class Solution(object):
    def totalFruit(self, fruits):
        f_basket =''
        s_basket =''
        l =0
        max_len=0
        if len(fruits)==1:
            return 1
        for r ,value in enumerate(fruits):
           
            if r==0:
                f_basket =[value,1]
                continue
            if f_basket[0] !=value and  s_basket =='':
                s_basket =[value,0]
                
            if value == f_basket[0]:
                f_basket[1] +=1
            
            if len(s_basket)>0 and value == s_basket[0]:
               
                s_basket[1] +=1
              
            while (f_basket[0] !=value and s_basket[0] !=value)  and ( f_basket[1]!=0 and s_basket[1] != 0):
               
               if fruits[l] == f_basket[0]:
                    f_basket[1] -=1   
               else:
                   s_basket[1] -=1
               l +=1
            max_len=max(max_len, r-l+1)
            if f_basket[1]  ==0:
                f_basket =[value,1]
            elif len(s_basket)>0 and s_basket[1] ==0:
                s_basket = [value ,1]
        return max_len