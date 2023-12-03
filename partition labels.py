class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        size = 0
        end = 0
        res = []

        for index, char in enumerate(s):
            last[char] = index

        for index, char in enumerate(s):
            size += 1
            if last[char] > end:
                end = last[char]
            
            if index == end:
                res.append(size)
                size = 0

        return res


"""
Time - O(1)
Sapce - O(n)
"""
