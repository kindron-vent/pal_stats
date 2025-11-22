# print("Welcome. This week is for working with data")
contacts = [

]
cmd = input("Type 'C'to create, 'R' to read, 'U' to update, 'D' to delete, 'V' to view all, or 'Q' to quit: ")
if cmd == 'q':
    print("Goodbye")

elif cmd == 'c':
    name = input("Enter name: ")
    number = input("Enter number: ")
    
    details= input("Enter details: ")
    new_contact = {
        "name": name,
        "number": number,
        "details": details 
    }
# Adding into the contact list
    contacts.append(new_contact)
    # put in a text file
    with open ("db.txt", "a") as file_handle:    #read the content in file
        file_handle.write(str(contacts))
    
    print("Contact created")
    print(contacts)

elif cmd == 'r':
    name = input("Enter name: ")
    for contact in contacts:
        if contact["name"] == name:
            print(f"{contact['name']}: {contact['number']}")
            break
    else:
        print("Contact not found")

# creating the records, system cannot read
# because the record was created in RAM which is volatile
# Thus need to create a file in hard drive for creating the records
# working with a file


# code to write to a file
# with open("db.txt", "w") as file_handle:  #writting a file
# with open ("db.txt", "r") as file_handle:    #read the content in file
    # content = file_handle.read()
    # content = file_handle.readlines()  #returns a list
    # print(content)
    # file_handle.write("Hello World") #created a file db.txt


# Appending/writting on  a file
# with open ("db.txt", "a") as file_handle:
#     file_handle.write("\n Woow wow wow wooow")