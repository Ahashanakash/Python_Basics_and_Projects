arr = input()
brr = arr[::-1]
if arr == brr:
    print(arr)
    print("YES")
else:
    yes = False
    point = 0
    for i in range(len(arr)):
        if brr[i] != "0":
            point = i
            break
    print(brr[point:])
    print("NO")
