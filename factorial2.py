#learning
# we can use conditional statement inside function definition.
# Calling function inside its own definition.




# factorial of given number 
def factorial(n): 

    # single line to find factorial 
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  
  

num = int(input("Enter the number :"))
print("Factorial of",num,"is", factorial(num)) 
  

