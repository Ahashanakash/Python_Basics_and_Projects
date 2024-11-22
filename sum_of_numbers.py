# a= int(input("Enter 1st number = "))
# b= int(input("Enter 2nd number = "))
# c= int(input("Enter 3rd number = "))
# print(a+b+c)

n = input("Enter numbers = ")
sum = 0
arr = list(map(int, n.split()))
for i in arr:
    sum += i
print(sum)
