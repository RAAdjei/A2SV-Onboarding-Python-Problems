class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        n = len(nums)
        minLeft = nums[0]

        for i in range(n):
            while stack and nums[i] >= stack[-1][0]:
                stack.pop()
            if stack and nums[i] > stack[-1][1]:
                return True
            stack.append([nums[i], minLeft])
            minLeft = min(nums[i], minLeft)
        
        return False

                 








        # for i in range(n):
        #     while stack and stack[-1] > nums[i] and len(stack) < 1:
        #         stack.pop()
        #     if len(stack) == 2:
        #         if stack[0] < nums[i] and stack[-1] > nums[i]:
        #             return True
        #             break
        #         else:
        #             stack[-1] = nums[i]
        #     else:
        #         stack.append(nums[i])

        #     print(stack)

        # return False


        
