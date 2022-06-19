#!/usr/bin/env python
# coding: utf-8

# In[53]:


import sys

print("....................................................................")
print("Hello dear user, welcome to our phone directory")
print("You may now proceed to explore this directory")
print("....................................................................")


def phonebook():
    rows, cols = int(input("Please enter number of contacts you want to add: ")), 4
    phone_book = []
    for row in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):" % (row+1))
        print("....................................................................")
        temp = []
        for col in range(cols):
                if col == 0:
                    temp.append(str(input("Enter name*: ")))
                    if temp[col] == '' or temp[col] == ' ':
                        sys.exit("Please enter Name of the Person it cannot leave blank")
                if col == 1:
                    temp.append(int(input("Enter number*: ")))
                if col == 2:
                    temp.append(str(input("Enter e-mail address: ")))
                    if temp[col] == '' or temp[col] == ' ':
                        temp[col] = None

                if col == 3:
                    temp.append(str(input("Enter date of birth(dd/mm/yyyy): ")))

                    if temp[col] == '' or temp[col] == ' ':
                        print("Date of birth cannot be Blank")
                        temp.append(str(input("Enter date of birth(dd/mm/yyyy) format:")))
    phone_book.append(temp)
    print(phone_book)
    return phone_book


def menu():
    print("********************************************************************")
    print("\t\t\tWELCOME TO PHONE DIRECTORY", flush=False)
    print("********************************************************************")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")
    ch=int(input("please enter your choice"))
    return ch


def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter name: ")))
        #if i == 1:
            dip.append(int(input("Enter number: ")))
        #if i == 2:
            dip.append(str(input("Enter e-mail address: ")))
        #if i == 3:
            dip.append(str(input("Enter date of birth(dd/mm/yyyy): ")))
        pb.append(dip)
        return pb
    
    
    
def remove_existing(pb):
    query = str(input("Please enter the name of the contact you wish to remove: "))
    temp = 0

    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            print(pb.pop(i))
            print("This query has now been removed")
    return pb
    
    if temp == 0:
        print("Sorry, you have entered an invalid query.\Please recheck and try again later.")
    return pb



def delete_all(pb):
    return pb.clear()

def search_existing(pb):
# This function searches for an existing contact and displays the result
    choice = int(input("Please Enter  1. Name:\n 2. DOB:\n "))
    temp = []
    check = -1

    if choice == 1:
        query = str(input("Please enter the name of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])
                
    if choice == 2:
#This will execute for searches based on contact''s date of birth
        query = str(input("Please enter the DOB (in dd/mm/yyyy format ONLY)of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][3]:
                check = i
                temp.append(pb[i])
            else:
                print("Invalid search criteria")
                return -1
            
    if check == -1:
        return -1
    else:
        display_all(temp)
        return check
    
    
def display_all(pb):
    if not pb:
        print("List is empty: []")
    else:
        for i in range(len(pb)):
            print(pb[i])
            
            
            
ch = 1
pb = phonebook()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb = remove_existing(pb)
    elif ch == 3:
        pb = delete_all(pb)
    elif ch == 4:
        d = search_existing(pb)
        if d == -1:
            print("The contact does not exist. Please try again")
    elif ch == 5:
        display_all(pb)
    elif ch==6:
        exit()
    else:
        print("invalid choice")


# In[ ]:





# In[ ]:




