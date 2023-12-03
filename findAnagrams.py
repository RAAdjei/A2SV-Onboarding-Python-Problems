class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        target_counts = collections.Counter(p)
        windows_counts = collections.Counter(s[:len(p)-1])

        for i in range(len(p) - 1, len(s)):
            windows_counts[s[i]] += 1
            if windows_counts == target_counts:
                result.append(i - len(p)+1)

            windows_counts[s[i - len(p) + 1]] -= 1
            if windows_counts[s[i-len(p)+1]] == 0:
                del windows_counts[s[i-len(p)+1]]

        return result

