class Solution(object):
    def isBoomerang(self, points):
         area=0
         area=0.5*(points[0][0]*(points[1][1]-points[2][1])+points[1][0]*(points[2][1]-points[0][1]) +points[2][0]*(points[0][1]-points[1][1]))
        
         if area!=0:
                return True
         else :
                return False