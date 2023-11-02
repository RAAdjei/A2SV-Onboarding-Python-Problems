class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        lent = len(nums)

        def backtracking(i, combo):
            if combo not in combinations:
                combinations.append(combo[:])

            if i >= lent:
                return

            combo.append(nums[i])
            backtracking(i+1, combo)
            combo.pop()

            backtracking(i+1, combo)
        
        backtracking(0, [])
        return combinations
