class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        visited = set()
        freq = Counter(s)
        stack = []

        for i in s:
            while stack and i <= stack[-1] and freq[stack[-1]] > 0 and i not in visited:
                visited.remove(stack[-1])
                stack.pop()
                
            if i not in visited:
                stack.append(i)
                visited.add(i)
            freq[i] -= 1
                
        return ''.join(stack)


            
            
        
