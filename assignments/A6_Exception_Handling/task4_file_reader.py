# task4_file_reader.py

filename = input("Enter filename: ")

try:
    file = open(filename, "r")
    
    print("First 3 lines:")
    for i in range(3):
        print(file.readline().strip())

    file.close()

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")

finally:
    print("File operation attempted.")
