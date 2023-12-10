t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    res = "YES"

    a.sort(reverse=True)
    
    while len(a) > 1:
        if a[-2] - a[-1] > 1:
            res = "NO"
            break
        a.pop()

    print(res)
