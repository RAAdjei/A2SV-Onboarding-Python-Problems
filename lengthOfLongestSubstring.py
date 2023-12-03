class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_str = 0
        letters = set()
        l = 0
        count = 0

        for i in range(len(s)):
            while s[i] in letters:
                letters.remove(s[l])
                l += 1
            letters.add(s[i])
            max_str = max(max_str, i-l+1)

        return max_str

"""
Time - O(N)
Space - O(N)
"""
