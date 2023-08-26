n, m = list(map(int, input().split()))
matrix = [list(input()) for i in range(n)]
res = ""

for i in range(n):
    for j in range(m):
        element = matrix[i][j]
        count = 0
        for cell in range(m):
            if element == matrix[i][cell]:
                count += 1
        for box in range(n):
            if element == matrix[box][j]:
                count += 1
                
        if count == 2:
            res += element
print(res)
