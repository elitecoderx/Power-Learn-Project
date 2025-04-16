def modify_content(content):
    return content.upper()

try:
    filename = input("Enter the filename to read: ")
    
    with open(filename, "r") as infile:
        content = infile.read()

    modified_content = modify_content(content)

    new_filename = "modified_" + filename
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"Modified content written to '{new_filename}'")

except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: Could not read the file.")