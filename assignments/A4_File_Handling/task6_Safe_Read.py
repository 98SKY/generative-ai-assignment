import os

filename = input("Enter filename: ")

if os.path.exists(filename):
    with open(filename, "r") as file:
        print("\nFile Content:\n")
        print(file.read())
else:
    print("File not found. Please check the filename.")
