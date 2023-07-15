class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = defaultdict(int)
        for price in bills:
            if price == 5:
                count[price] += 1
            elif price == 10:
                count[price] += 1
                count[5] -= 1
                if count[5] < 0:
                    return False
            elif price == 20:
                count[price] += 1
                if count[10] >= 1 and count[5] >= 1:
                    count[10] -= 1
                    count[5] -=1
                elif count[5] >= 3:
                    count[5] -= 3
                
                else:
                    return False
        return True
