lines = ["First line\n", "Second line\n", "Third line\n"]

with open("my_file.txt", "w") as file:
    file.writelines(lines)
