class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()
        count = {i:0 for i in range(numCourses)}
        res = []

        adj = defaultdict(list)
        
        for key, val in prerequisites:
            adj[val].append(key)
            count[key] += 1

        for i in count:
            if count[i] == 0:
                queue.append(i)        
        
        while queue:
            cur_course = queue.popleft()
            res.append(cur_course)

            for neighbour in adj[cur_course]:
                count[neighbour] -= 1
                if count[neighbour] == 0:
                    queue.append(neighbour)

            
        return (res if len(res) == numCourses else [])




            
