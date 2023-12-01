class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # adj_list = defaultdict(list)

        # for row in range(len(image)):
        #     for col in range(len(image[row])):
        #         if image[row][col] == 1:
        #             adj_list[row].append(col)

     
    
        directions = [(1, 0),(-1, 0), (0, 1), (0, -1)]
        start_node = image[sr][sc]
        visited = []
        image[sr][sc] = color


        def inbound(node):
            if  0 <= node[0] < len(image) and 0 <= node[1]< len(image[0]):
                return True
            
            return False

        def dfs(node, visited):
            # visited.add(node)
            visited.append(node)

            for direction in directions:
                new_node = [direction[0]+node[0], direction[1]+node[1]]
                if inbound(new_node) and new_node not in visited:
                    if image[new_node[0]][new_node[1]] == start_node:
                        
                        image[new_node[0]][new_node[1]] = color
                        dfs(new_node, visited)

        dfs([sr,sc], visited)

        return image




        

            


