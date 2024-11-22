number = int(input("Enter number = "))

if number>= 80:
    print("A+")
elif number>=75 and number<80:
    print("A")
elif number>=70 and number<75:
    print("A-")
elif number>=65 and number<70:
    print("B+")
elif number>=60 and number<65:
    print("B")
elif number>=55 and number<60:
    print("B-")
elif number>=50 and number<55:
    print("C+")
elif number>=45 and number<50:
    print("C")
elif number>=40 and number<45:
    print("D")
else:
    print("F")