t = int(input())
 
for _ in range(t):
    new = []
    n = int(input())
    nums = list(map(int, input().split()))
    left = 0
    right = len(nums)-1
    
    while left <= right:
        new.append(nums[left])
        
        if left != right:
            new.append(nums[right])
        left += 1
        right -= 1
            
