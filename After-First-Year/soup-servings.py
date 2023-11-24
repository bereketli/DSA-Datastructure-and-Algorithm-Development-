class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4500:
            return 1.0
        operations = [[-100, 0], [-75, -25], [-50, -50], [-25, -75]]
        memo = {}
        def probability(x, y):
            if (x, y) in memo:
                return memo[(x, y)]

            if x <= 0 and y <= 0:
                return [0.0, 1.0, 0.0]
            if x <= 0:
                return [1.0, 0.0, 0.0]
            if y <= 0:
                return [0.0, 0.0, 1.0]

            prob = [0.0, 0.0, 0.0]
            for a, b in operations:
                next_prob = probability(x + a, y + b)
                prob[0] += 0.25 * next_prob[0]
                prob[1] += 0.25 * next_prob[1]
                prob[2] += 0.25 * next_prob[2]

            memo[(x, y)] = prob
            return prob

        final_probabilities = probability(n, n)
        return final_probabilities[0] + (final_probabilities[1] / 2.0)
