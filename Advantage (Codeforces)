import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


t =inp()

for _ in range(t): 
    n = inp() 
    a = inlt()
    max_num = max(a)
    sort_a = sorted(a)
    res = []
    
    for i in range(n):
        if a[i] == max_num:
          ans =  a[i] - sort_a[-2]
          res.insert(i ,ans)
          
        else:
            ans = a[i] - max_num
            res.append(ans)
            
    print(*res)


"""
Time - O(nLogn)
Space - O(N)
"""
