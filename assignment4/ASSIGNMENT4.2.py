def main():
    initial_text = input("Enter text to write to the file: ")
    with open("output.txt", "w") as file:
        file.write(initial_text)
    print("Data successfully written to output.txt.")
    print()

    # Appending file
    additional_text = input("Enter additional text to append: ")
    with open("output.txt", "a") as file:
        file.write("\n" + additional_text)
    print("Data successfully appended.")
    print()

    # display final content
    print("Final content of output.txt:")
    with open("output.txt", "r") as file:
        content = file.read()
        print(content)

if __name__ == "_main_":
    main()