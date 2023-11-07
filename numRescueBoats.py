class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people)-1
        count = 0
        people.sort()

        
        while l <= r:
            leftover = limit - people[r]
            count += 1
            r -= 1
            if people[l] <= leftover and l <= r:
                l += 1

        return count


"""
Time - O(NlogN)
Space - O(1)
"""
        
