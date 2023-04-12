class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        totalSkill = skill[0] + skill [-1]
        product = skill [0] * skill [-1]
        left = 1
        right = len(skill) - 2
        while left < right:
            if skill[left] + skill[right] != totalSkill:
                return -1
            else:
                product += skill[left] * skill[right]
                left += 1
                right -= 1
        return product
