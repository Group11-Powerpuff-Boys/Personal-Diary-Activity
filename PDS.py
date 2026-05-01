filename = "Diary.txt"

try:
    f = open(filename, "x")
    f.close()
except FileExistsError:
    print("File already exists")

def searchDiary(Searchdate):
    try:
        with open(filename, "r") as f:
            entry = f.readlines()
        datematch = []

        for i, key in enumerate(entry, 1):
            if Searchdate in key:
                datematch.append((i, key.strip()))
        
        if datematch:
            print("\n")
            print(f"Entry {Searchdate} Found!")
            for index, message in datematch:
                print(f"{index}: {message}")
            print("\n")
        else:
            print("Entry Not Found!\n")
    except FileNotFoundError:
        print("File not Found")

def deleteEntry(Searchdate):
    try:
        with open(filename, "r") as f:
            entry = f.readlines()
        datematch = []
        
        for deldate in entry:
            if Searchdate not in deldate:
                datematch.append(deldate)

        with open(filename, "w") as f:
            f.writelines(datematch)
        
        print(f"Deleted entry {Searchdate}!\n")
    except FileNotFoundError:
        print("File not Found")


while True:
    print("Personal Diary Application")
    print("1. Add Diary Entry")
    print("2. View Diary Entries")
    print("3. Search a Diary Entry")
    print("4. Delete a Diary Entry")
    print("5. Exit")

    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            try:
                date = input("(DAY/MONTH/YEAR): ")
                diary = input("Write your diary: ")

                if not date.strip() or not diary.strip():
                    raise Exception
                else:
                    with open(filename, "a") as f:
                        f.write(date + " " + diary + "\n")

                print("Diary added successfully!\n")

            except Exception as error:
                print("An error occurred while adding the diary:", error)
        elif choice == 2:
            try:
                with open(filename, "r") as f:
                    content = f.read()
                    if content.strip() == "":
                        print("No diary entries found.\n")
                    else:
                        print("\n--- Diary Entries ---")
                        print(content)
                        print("---------------------")
            except FileNotFoundError:
                print("Diary file not found.")
        elif choice == 3:
            try:
                Searchdate = input("Enter a date(Day/Month/Year): ")
                if not Searchdate.strip():
                    raise ValueError
            except ValueError as e:
                print("Invalid Input")
            else:
                searchDiary(Searchdate)
        elif choice == 4:
            try:
                Searchdate = input("Enter a date(Day/Month/Year): ")
                if not Searchdate.strip():
                    raise ValueError("Empty string")
            except ValueError as e:
                print("Invalid Input")
            else:
                deleteEntry(Searchdate)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Error! Try Again")
    except ValueError:
        print("Invalid Input")