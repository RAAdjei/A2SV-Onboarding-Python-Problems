class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        n = len(nums)
        i = 0

        while i < n:
            idx = nums[i]-1
            if nums[i] != i+1 and nums[idx] != nums[i]:
                nums[idx], nums[i] = nums[i], nums[idx]
            else:
                i += 1

        output = [nums[i] for i in range(n) if nums[i] != i+1]

        return output
        
