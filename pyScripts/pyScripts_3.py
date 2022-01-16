
ContactDetails = {}

def checkUserExist(name):
    for c in ContactDetails.keys():
        if c == name:
            return True;
    return False

def insert():
    print("Enter Your Name: ")
    name = input()
    print("Enter Your contact number : ")
    contact = []
    con = input()
    contact.append(con)
    print("want to enter alternative number ?(Y/N)")
    mul = input()
    if mul == "Y":
        print("Enter Alternative number : ")
        con = input()
        contact.append(con)

    if checkUserExist(name):
        print("User Already Exits..Try to enter diffrent name")
    else:
        ContactDetails[name] = contact

def viewAll():
    print("***********************************")
    for c in sorted(ContactDetails):
        print(c + ": " + str(ContactDetails.get(c)))
    print("***********************************")

def search():
    print("===================================")
    print("Enter name you want to search:")
    name = input()
    print("***********************************")
    for c in sorted(ContactDetails):
        if name in c:
            print(c + ": " + str(ContactDetails.get(c)))
    print("***********************************")


if __name__ == "__main__":
    choice = 0
    while True:
        print("===================================")
        print("Enter 1 for insert")
        print("Enter 2 for View All")
        print("Enter 3 for Search")
        print("Enter 4 for Exit")
        print("===================================")
        print("Enter Your Choice : ")
        choice = int(input())

        if choice == 1:
            insert()
        elif choice == 2:
            viewAll()
        elif choice == 3:
            search()
        else:
            print("Thank You")
            break;


