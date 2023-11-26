class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for asteroid in asteroids:
            while result and result[-1] > 0 and asteroid < 0:
                if result[-1] + asteroid < 0:
                    result.pop()
                elif result[-1] + asteroid > 0:
                    break
                else:
                    result.pop()
                    break
            else:
                result.append(asteroid)
        return result