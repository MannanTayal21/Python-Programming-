file_path = 'example.txt'  # Replace with your file path

try:
    file = open(file_path, 'r')
    content = file.read()
    print("File content:\n", content)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except IOError:
    print(f"Error: Could not read the file '{file_path}'.")
finally:
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("File was never opened, so nothing to close.")
