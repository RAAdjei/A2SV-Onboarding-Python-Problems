class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(vertex, visited):
            if vertex == destination:
                return True
            
            visited.add(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    found = dfs(neighbour, visited)

                    if found:
                        return True
                    else:
                        False
                    


        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        visited = set()

        return dfs(source, visited)

"""
Time - O(N^2)
Space - O(N)
"""
