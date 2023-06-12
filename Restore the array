test_cases = int(input())

for _ in range(test_cases):
    new_len = int(input())
    input_arr = list(map(int, input().split()))
    new_arr = [0]*(new_len)
    
    new_arr[0] = input_arr[0]
    
    for i in range(new_len - 2):
        new_arr[i+1] = min(input_arr[i], input_arr[i+1])
        
    new_arr[-1] = input_arr[-1]
    
    print(*new_arr)
