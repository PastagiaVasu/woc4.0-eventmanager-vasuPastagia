
ContactDetails = {}
IDs = []
cnt = 0

def displayRecords():
    for e in IDs:
        print(ContactDetails[e]["name"] + " : " + ContactDetails[e]["contact"])

if __name__ == "__main__":
    choice = 0
    while choice != 4:
        print("Enter 1 to Insert Data")
        print("Enter 2 for view all Data")
        print("Enter 3 fro Search")
        print("Enter Your Choice : ")
        choice = int(input())
        # Insert
        if choice == 1:
            print("Enter Your name:")
            name = input()
            print("Enter Your Contact No: ")
            contact = input()
            if len(contact) < 10:
                print("Please Enter Valid Contact Number(10 digits only)")

            emp = {"name": name, "contact": contact}
            ContactDetails["emp" + str(cnt)] = emp
            IDs.append("emp" + str(cnt))
            cnt += 1
        # View All Data
        elif choice == 2:
            displayRecords()
        # Search Code Starts from here
        elif choice == 3:
            print("Enter 1 for Name Wise search")
            print("Enter 2 for Contact number wise search")
            ch = int(input())
            if ch == 1:
                print("Enter Name you want to search: ")
                name = input()
                for e in IDs:
                    if ContactDetails[e].get("name") == name:
                        details = ContactDetails[e]
                if len(details) > 0:
                    print(details["name"] + " : " + details["contact"])
                    details.clear()
                else:
                    print("No Data Found")
            elif ch == 2:
                print("Enter Contact you want to search: ")
                con = input()
                for e in IDs:
                    if ContactDetails[e].get("contact") == con:
                        details = ContactDetails[e]

                if len(details) > 0:
                    print(details["name"] + " : " + details["contact"])
                    details.clear()
                else:
                    print("No Data Found")

            # print("Enter Data You Want to Search: ")
            # data = input()
            # for e in IDs:
            #     if ContactDetails[e]["name"] == data:
            #         details = ContactDetails[e]
            #     elif ContactDetails[e]["contact"] == data:
            #         details = ContactDetails[e]
            # if len(details) > 0:
            #     print(details["name"] + " : " + details["contact"])
            #     details.clear()
            # else:
            #     print("No Data Found")



