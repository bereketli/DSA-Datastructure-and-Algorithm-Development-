import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        word_count = [(-count[word], word ) for word in count]
        heapq.heapify(word_count)
        output = []
        for i in range (k):
            output.append(heapq.heappop(word_count)[1])
        return output

        
        
