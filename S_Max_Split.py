s = input()
ss = []
l = r = cnt = start = 0
for i, c in enumerate(s):
    if c == "L":
        l += 1
    else:
        c == "R"
        r += 1
    if l == r:
        cnt += 1
        ss.append(s[start : i + 1])
        l = r = 0
        start = i + 1
print(cnt)
for i in ss:
    print(i)