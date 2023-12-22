class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        queue = deque()
        adj = defaultdict(list)
        safe = []
        neighbours = defaultdict(list)

        outgoing = {i:0 for i in range(len(graph))}

        for key in range(len(graph)):
            for i in graph[key]:
                adj[i].append(key)
                outgoing[key] += 1

        for i in outgoing:
            if outgoing[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            safe.append(node)

            for neighbour in adj[node]:
                outgoing[neighbour] -= 1
                if outgoing[neighbour] == 0:
                    queue.append(neighbour)

        safe.sort() 
        return safe                     
        
