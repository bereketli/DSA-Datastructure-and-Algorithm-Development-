class Player:
    def __init__(self, age, score):
        self.age = age
        self.score = score
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        players = []
        dp = [0] * n

        for i in range(n):
            players.append(Player(ages[i], scores[i]))

        players.sort(key=lambda x: (-x.age, -x.score))

        for i in range(n):
            dp[i] = players[i].score
            for j in range(i):
                if players[j].score >= players[i].score:
                    dp[i] = max(dp[i], dp[j] + players[i].score)

        return max(dp)

        
