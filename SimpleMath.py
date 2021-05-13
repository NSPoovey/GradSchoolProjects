num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y != 0:
        return x/y
print(num1, "+", num2, "=", add(num1,num2))
print(num1, "-", num2, "=", subtract(num1,num2))
print(num1, "*", num2, "=", multiply(num1,num2))
print(num1, "/", num2, "=", divide(num1,num2))