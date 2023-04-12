class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.paths = []
        def allpath(arr, idx):
            for i in range(len(self.graph[idx])):
                arr.append(self.graph[idx][i])
                if arr[-1] == len(self.graph) - 1:
                    self.paths.append([] + arr)
                    arr.pop()
                    continue
                allpath(arr,self.graph[idx][i] )
                arr.pop()
            return
        allpath([0],0)
        return self.paths
