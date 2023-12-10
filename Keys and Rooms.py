class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys_visited = set([0])
        queue = deque()

        queue.append(rooms[0])

        while queue:
            boundary = len(queue)

            for _ in range(boundary):
                room = queue.popleft()

                for key in room:
                    if key not in keys_visited:
                        keys_visited.add(key)
                        queue.append(rooms[key])

        return len(keys_visited) == len(rooms)

              
