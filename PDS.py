try:
    f = open("Diary.txt", "x")
    f.write("04/28/2026")
    f.close()
except FileExistsError:
    print("File not Found")


while True:
    print("Personal Diary Application");
    print("1. Add Diary Entry");
    print("2. View Diary Entries");
    print("3. Exit");
    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            try:
                diary = input("Write your diary: ")
                with open("Diary.txt", "a") as f:
                    f.write(diary + "\n")
                print("Diary added successfully!")

            except Exception as error:
                print("An error occurred while adding the diary:", error)
            
        elif choice == 2:
            print("view")
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Error! Try Again")
    except ValueError:
        print("Invalid Input")
