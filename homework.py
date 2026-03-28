names = []

while True:
    print("\n------- NAME MANAGEMENT MENU -------")
    print("1. Add a name")
    print("2. Change a name")
    print("3. Delete a name")
    print("4. View all names")
    print("5. Exit program")
    
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        new_name = input("Enter the name to add: ")
        names.append(new_name)
        print(f"'{new_name}' has been added.")


    elif choice == "2":
        if len(names) == 0:
            print("The list is empty. Nothing to change.")
        else:
            print("Current names:", names)
            old_name = input("Enter the name you want to change: ")
            if old_name in names:
                new_name = input("Enter the new name: ")
                index = names.index(old_name)
                names[index] = new_name
                print(f"'{old_name}' has been changed to '{new_name}'.")
            else:
                print("That name is not in the list.")


    elif choice == "3":
        if len(names) == 0:
            print("The list is empty. Nothing to delete.")
        else:
            print("Current names:", names)
            del_name = input("Enter the name to delete: ")
            if del_name in names:
                names.remove(del_name)
                print(f"'{del_name}' has been deleted.")
            else:
                print("That name is not in the list.")


    elif choice == "4":
        if len(names) == 0:
            print("The list is empty.")
        else:
            print("\n--- List of Names ---")
            for i, name in enumerate(names, start=1):
                print(f"{i}. {name}")

    elif choice == "5":
        print("Exiting program. Goodbye")
        break

    else:
        print("Invalid choice. Please select a number between 1 and 5.")
