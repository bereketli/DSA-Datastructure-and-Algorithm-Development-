class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        output = []
        for num in count_dict.most_common(k):
          output.append(num[0])
        return output