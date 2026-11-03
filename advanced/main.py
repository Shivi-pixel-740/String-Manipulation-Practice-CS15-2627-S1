while True:
    print("Choose how you would like to process a string:")
    print()
    print("1. Format a Name")
    print("2. Format a Title")
    print("3. Format a List")
    print("4. Process Numbers")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        string_to_process = input("Enter the name to process: ")

        cleaned_name = string_to_process.strip()

        name_parts = cleaned_name.split(",")
        if len(name_parts) != 2:
            print("Invalid name. Please enter a last name and first name separated by a comma.")

        else:
            last_name = name_parts[0].strip().title()
            first_name = name_parts[1].strip().title()

            if last_name == "" or first_name == "":
                print("Both names must be entered.")

            else:
                print(first_name + " " + last_name)



    elif choice == "2":
        string_to_process = input("Enter the title to process: ")
        if string_to_process.strip() == "":
            print("Please enter a title.")

        elif choice == "2":
            string_to_process = input("Enter the title to process: ")

            if string_to_process.strip() == "":
                print("Please enter a title.")

            else:
                parts = string_to_process.replace(",", "|").replace("::", "|").split("|")

                formatted_words = []

                for word in parts:
                    formatted_words.append(word.replace(" ", "").title())

                formatted_title = " ".join(formatted_words)

                print(formatted_title)

    elif choice == "3":
        string_to_process = input("Enter the list to process: ")

        if string_to_process.strip() == "":
            print("Please enter at least one item.")

        else:
            items = string_to_process.split(",")

            uppercase_items = []

            for item in items:
                if item.strip() == "":
                    print("Invalid list. Please do not leave empty items.")
                    break

                uppercase_items.append(item.strip().upper())

            else:
                formatted_list = " | ".join(uppercase_items)

                print(formatted_list)
    elif choice == "4":
        string_to_process = input("Enter the numbers to process: ")

        try:
            cleaned_numbers = string_to_process.strip()

            if cleaned_numbers == "":
                print("Please enter at least one number.")

            else:
                number_parts = cleaned_numbers.split(",")

                numbers = []

                for number in number_parts:
                    numbers.append(int(number.strip()))

                total = sum(numbers)
                average = total / len(numbers)

                print("Total:", total)
                print("Average:", average)

        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
