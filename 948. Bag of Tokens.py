class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()
        maxscore =0
        score =0
        l, r =0, len(tokens) -1
        while l <=r:
            if power >= tokens[l]:
                score += 1
                maxscore = max(maxscore, score)
                power -= tokens[l]
                l +=1
            elif score > 0:
                score -=1
                power += tokens[r]
                r -=1
            else:
                break
        return maxscore


        """
        while l < r:
            power > tokens[i]:
            powers -= tokens[l]
            score +=1
            else:
                score -=1
                power +=tokens[r]
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        