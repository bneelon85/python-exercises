import pickle
phoneBook = {"Bobby": "281-750-2912", "Kris":"832-586-5055"}
print("Electronic Phone Book\n=====================\n1. Look up an entry\n2. Set an entry\n3. delete and entry\n4. List all entries\n5. Save Entries to File\n6. Restore saved entries\n7.Quit")
selection = input("What do you want to do (1-7)?")
while(int(selection) !=7):
    if(int(selection) == 1):
        name = input("Name: ")
        print(name,"'s Phone Number is: ",phoneBook[name],"\n", sep ="")
    elif(int(selection) == 2):
        nameIn = input("What is the entry's name? ")
        phoneIn = input("Phone number: ")
        phoneBook[nameIn] = phoneIn
        print("Entry stored for",nameIn,"\n")
    elif(int(selection) == 3):
        nameDel = input("Whom would you like to remove from the phone book? ")
        del phoneBook[nameDel]
        print(nameDel,"has been deleted from the phone book.\n")
    elif(int(selection) == 4):
        for key, value in phoneBook.items():
            print("Name:",key,"     Phone Number:",value,"\n")
    elif(int(selection) == 5):
        pbFile = open('phonebook.pickle', 'wb')
        pickle.dump(phoneBook, pbFile)
        pbFile.close()
        print("Entries saved to file.\n")
    elif(int(selection) == 6):
        pbOpen = open('phonebook.pickle','rb')
        phoneBook = pickle.load(pbOpen)
        print('Entries restored.\n')
    elif(int(selection)<1 or int(selection)>7):
        print("Invalid Entry\n")
        
    print("Electronic Phone Book\n=====================\n1. Look up an entry\n2. Set an entry\n3. delete and entry\n4. List all entries\n5. Save Entries to File\n6. Restore saved entries\n7.Quit")
    selection = input("What do you want to do (1-7)?")
print("Thank you for using the Phone Book. Goodbye!")