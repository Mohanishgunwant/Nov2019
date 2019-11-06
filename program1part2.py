#Python Program to Check if a Number is Positive, Negative or 0- using nested conditional statements.



num = float(input("Enter the number: "))


if num >= 0:
    if num == 0:
        print("number is zero")
    else:
        print("number is positive")
else:
    print("number is negative")


