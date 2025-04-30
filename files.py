try:
    user_input = input("Enter the file path: ")

    with open(user_input, "r") as file:
        data = file.read()
        print("Original file content:\n", data)

    # Modify the content (capitalize the first character only)
    modified_data = data.capitalize()

    modified_file = "modified_out.txt"

    with open(modified_file, "w") as file:
        file.write(modified_data)

    print(f"\nModified content written to '{modified_file}'.")

except FileNotFoundError:
    print("File not found. Please check the file path and try again.")

except Exception as e:
    print(f"An error occurred: {e}")
