class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radius =0
        h_p =0
        for house in houses:
            while h_p < len(heaters)-1 and house >= heaters[h_p+ 1]:
                h_p +=1
              
            if h_p < len(heaters)-1:
                radius = max(radius,min(abs(house - heaters[h_p]),abs(house - heaters[h_p +1 ])))
            else: 
                radius =max( radius,abs(house - heaters[h_p]) )
         
        return radius
