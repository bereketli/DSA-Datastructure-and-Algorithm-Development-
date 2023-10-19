class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        left_candy = [1] * N
        right_candy = [1] * N

        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                left_candy[i] = left_candy[i - 1] + 1

        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right_candy[i] = right_candy[i + 1] + 1

        res = 0
        for i in range(N):
            res += max(left_candy[i], right_candy[i])

        return res


