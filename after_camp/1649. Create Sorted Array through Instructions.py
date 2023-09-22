class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = 10 ** 9 + 7
        max_val = max(instructions)
        bit = [0] * (max_val + 1)

        def update(idx, val):
            while idx <= max_val:
                bit[idx] += val
                idx += idx & -idx

        def query(idx):
            result = 0
            while idx > 0:
                result += bit[idx]
                idx -= idx & -idx
            return result

        cost = 0
        for i, instruction in enumerate(instructions):
            left_count = query(instruction - 1)
            right_count = i - query(instruction)
            cost += min(left_count, right_count)
            update(instruction, 1)

        return cost % mod
