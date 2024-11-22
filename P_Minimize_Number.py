n = int(input())
arr = list(map(int, input().split()))

mn = 1e9 + 7
for i in arr:
    cnt = 0
    while i > 0:
        if i % 2 == 0:
            cnt += 1
            i = i / 2
            continue
        else:
            break
    if cnt < mn:
        mn = cnt
print(mn)
