t = int(input())
 
for i in range(t):
    n = int(input())
    robots = list(map(int, input().split()))
    
    max_robot = max(robots)
    count = [0] * (max_robot + 1)
    
    for num in robots:
        count[num] += 1
        
    for i in range(len(count) - 1):
        if count[i] < count[i+1]:
            print("NO")
            break
    else:
        print("YES")
