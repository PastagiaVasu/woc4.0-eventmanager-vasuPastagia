# basic calc
num1 = float(input("Enter first number : "))
operation = input("Which operation you want ( +,-,*,/)")
num2 = float(input("Enter Another number : "))
# res=float(num1)+float(num2)
# print("Sum of this two numbers: "+str(res))
# print("Division of given numbers: "+str(float(num1)/float(num2)))

# BIt advanced calc

if operation == "+":
    print("Sum of two numbers: " + str((num1+num2)))
elif operation == "-":
    print("Subtraction : " + str((num1 - num2)))
elif operation == "*":
    print("Multiplication : " + str((num1 * num2)))
elif operation == "/":
    print("Division : " + str((num1 / num2)))
else:
    print("Invalid Operator")