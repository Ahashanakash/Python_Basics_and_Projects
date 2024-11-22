# a= int(input("Enter 1st number = "))
# b= int(input("Enter 2nd number = "))
# c= int(input("Enter 3rd number = "))

# if a>=b and a>=c:
#     print(a," is greater")
    
# elif b>=c and b>=a:
#     print(b," is greater")

# elif c>=b and c>=a:
#     print(c," is greater")
    
    
arr = input("Enter 3 numbers = ")
n=list(map(int,arr.split()))
print(max(n))