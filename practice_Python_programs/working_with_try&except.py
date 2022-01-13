# basically used to catch run time error

# try:
#     num = int(input("Enter number: "))
#     print(num)
# except:
#     print("Invalid input")

try:
    val = 10/2
    num = int(input("Enter number: "))
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)