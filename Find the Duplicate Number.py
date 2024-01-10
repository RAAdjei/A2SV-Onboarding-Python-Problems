class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            idx = nums[i]-1
            if nums[i] != i+1 and nums[idx] != nums[i]:
                nums[idx], nums[i] = nums[i], nums[idx]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i+1:
                res = nums[i]

        return res
        
