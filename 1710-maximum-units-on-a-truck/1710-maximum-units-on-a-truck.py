class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
       
        def secondItem(element):
              return element[1]

        sum=0
        i=0
        
        boxTypes.sort(reverse=True ,key=secondItem)
        counted=boxTypes[0][0]

        while(truckSize-counted>0 and len(boxTypes)>i):
             if(len(boxTypes)-i>1):
                    counted+=boxTypes[i+1][0]
             sum+=boxTypes[i][0]*boxTypes[i][1]
    
             i+=1
        if(truckSize-counted<0):
            if (i==0):
              sum+=truckSize*boxTypes[i][1]
            else:
               
              sum+=((boxTypes[i][0]-(counted-truckSize)))*boxTypes[i][1]
        if(truckSize-counted==0):
             sum+=boxTypes[i][0]*boxTypes[i][1]
        return sum

          