n = int(input())
ar = input()
arr = list(map(int, ar.split()))

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

ans = 0

for i in freq:
    x = freq[i]
    if x < i:
        ans += x
    else:
        ans += abs(x - i)

print(ans)
