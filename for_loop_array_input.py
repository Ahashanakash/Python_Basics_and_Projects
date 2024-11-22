n = input("Enter array = ")

arr = list(map(int, n.split()))

print("Array = ", end=" ")
for i in arr:
    print(i, end=" ")