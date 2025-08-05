file_name = input("Enter the path to the TXT File: ")

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        print("n/ File content")
        print(content)

except FileNotFoundError:
    print("File not found. Please check the file path")

except Exception as e:
    print(f"An error occurend {e}")
