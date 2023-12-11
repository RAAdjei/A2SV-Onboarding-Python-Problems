t = int(input())

for _ in range(t):
    num_cubes = int(input())
    cubes = list(map(int, input().split()))
    count = 0
    
    for j in range(1, num_cubes):
        if cubes[j-1] > cubes[j]:
            count += 1
    
    if count != num_cubes-1:
        print("YES")
    else:
        print("NO")
        
