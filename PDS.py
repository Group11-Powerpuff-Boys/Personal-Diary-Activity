from datetime import datetime

try:
    f = open("Diary.txt", "x")
    f.close()
except FileExistsError:
    print("File already exists")

while True:
    print("\nPersonal Diary Application")
    print("1. Add Diary Entry")
    print("2. View Diary Entries")
    print("3. Exit")

    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            try:
                diary = input("Write your diary: ")
                now = datetime.now()
                date_time = now.strftime("%m/%d/%Y %I:%M %p")

                with open("Diary.txt", "a") as f:
                    f.write(f"[{date_time}] {diary}\n")

                print("Diary added successfully!")

            except Exception as error:
                print("An error occurred while adding the diary:", error)

        elif choice == 2:
            try:
                with open("Diary.txt", "r") as f:
                    content = f.read()
                    if content.strip() == "":
                        print("No diary entries found.")
                    else:
                        print("\n--- Diary Entries ---")
                        print(content)
                        print("---------------------")
            except FileNotFoundError:
                print("Diary file not found.")

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Error! Try Again")

    except ValueError:
        print("Invalid Input")