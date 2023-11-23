class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        res = 0
        for i in graph:
            if len(graph[i]) > 1:
                res = i
                break

        return res 

"""
Time - O(N)
Space - O(N)
"""
        
