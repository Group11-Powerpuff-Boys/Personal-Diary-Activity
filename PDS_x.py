
while True:

    print("Personal Diary Application");
    print("1. Add Diary Entry");
    print("2. View Diary Entries");
    print("3. Exit");
    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            print("Add")
        elif choice == 2:
            print("view")
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Error! Try Again")
    except ValueError:
        print("Invalid Input")


