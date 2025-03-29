with open("example.txt", "w") as file:
    lines = ["Hello, World!\n", "Python file"]
    file.writelines(lines)  

print("Data written successfully!")
