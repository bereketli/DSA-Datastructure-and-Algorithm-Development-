class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.leader  = {}
        self.counter = {}
        maximum = [0, 0]
        for i in range(len(persons)):
            if  persons[i] not in  self.counter:
                self.counter[persons[i]] = 1
            else:
                self.counter[persons[i]] += 1
            if self.counter[persons[i]] >= maximum[1]:
                maximum = [persons[i], self.counter[persons[i]]]
            self.leader[i] = maximum[0]
      
    def q(self, t: int) -> int:
        l = 0
        r = len(self.times) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.times[mid] >  t:
                r = mid - 1
            elif self.times[mid] < t:
                l = mid + 1
            else:
                return self.leader[mid]
        return  self.leader[l - 1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
"""
person = [0,1,1,0], time = [0,5,10, 15]
leader_atindex = {
    0 : 1
    1 :1
    2 :1

}
maximum = [0,0]
counter = {
    0:1
    1:2
}




"""
