n = int(input()) 
skills = list(map(int, input().split()))

l = 0
r = 0
max_num = 0
count = 0

if len(skills) == 1:
     print(1)
     exit()

skills.sort()


while r < n:
    if skills[r] - skills[l] <= 5:
        count += 1
        max_num = max(max_num, count)
        r += 1

    else:
        count -= 1
        l += 1

print(max_num)
