class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if len(stack) == 0 or stack[-1][0] != char:
                stack.append([char, 1])
            else:
                stack[-1][1] += 1

            if stack[-1][1] == k:
                stack.pop()

        return "".join([char * count for char, count in stack])


"""
Time = O(N)
Space = O(N)
"""




        # stack = [0]
        # lent = len(s)

        # for i in range(lent):
        #     stack.append(s[i])
        #     pt = -1
        #     count = 1
        #     while count != k and count < len(stack) and stack[pt] == stack[pt-1]:
        #         if stack[pt] == stack[pt-1]:
        #             count += 1
        #             pt -= 1
        #     if count == k:
        #         stack = stack[:len(stack)-k]

        # res = "".join(stack[1:])
        # return res
                         
                
            
