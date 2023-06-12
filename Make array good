def power_of_two(num):
    current = 1
    
    while current <= num:
        current *= 2
    return current

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(n)
    
    for i in range(1, n+1):
        print(i, power_of_two(arr[i-1]) - arr[i-1])
