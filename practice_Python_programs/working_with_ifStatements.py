
is_male = True

if is_male:
    print("Hey Man")
else:
    print("Hey Women")

is_tall = False

if is_male or is_tall:
    print("You are man or tall or both")
else:
    print("You are neither tall or male")

if is_male and is_tall:
    print("You are man and tall")
elif is_male and not(is_tall):
    print("you are man but not tall")
else:
    print("You are neither tall or male")

# If statement with comparision
