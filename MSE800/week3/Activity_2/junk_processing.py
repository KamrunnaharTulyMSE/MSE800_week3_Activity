# Week 3 Activity 2 - Junk file processing

def main():
    # Open the original file and read all text.
    with open("junk.txt", "r", encoding="utf-8") as file:
        text = file.read()

    # Count the number of lines in the original file.
    line_count = len(text.splitlines())
    print("Total number of lines:", line_count)

    # Convert all text to lowercase.
    text = text.lower().rstrip("\n")

    # Add the required line at the end.
    text += "\ntext file nanalyssis\n"

    # Save the processed file.
    with open("junk_processed.txt", "w", encoding="utf-8") as file:
        file.write(text)

    print("Processed file saved as junk_processed.txt")


if __name__ == "__main__":
    main()
