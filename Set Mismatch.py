class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
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
                dup = nums[i]
                missing = i+1
        

        return [dup, missing]
        
