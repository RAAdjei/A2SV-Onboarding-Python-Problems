class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()

        adj_list = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    adj_list[i+1].append(j+1)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for neighbour in adj_list[node]:
                dfs(neighbour)
        
        count = 0
        for pro in adj_list.keys():
            if pro not in visited:
                dfs(pro)
                count += 1

        return count


"""
Time - O(n^2)
Space - O(n)
"""
