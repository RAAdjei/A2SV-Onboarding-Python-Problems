class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        stones = [-i for i in stones]

        heapq.heapify(stones)     

        while len(stones) > 1:
            print(stones)
            st1 = heapq.heappop(stones)
            st2 = heapq.heappop(stones)
            if st1 != st2:
                diff = abs(st1) - abs(st2)
                heapq.heappush(stones, -diff)

        if len(stones) >= 1:
            return abs(stones[0])
        else:
            return 0


"""
Time - O(N)
Space - O(N)
"""


        
