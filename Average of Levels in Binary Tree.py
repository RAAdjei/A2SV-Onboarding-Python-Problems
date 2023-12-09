# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        ave = []

        while queue:
            boundary = len(queue)
            total = 0

            for _ in range(boundary):
                curr = queue.popleft()
                total += curr.val

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            ave.append(total/boundary)

        return ave


        
