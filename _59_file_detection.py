# Python file detection
#
import os

file_path1 = "_59_1_test.txt"  # relative file path
file_path2 = "stuff/_59_1_test.txt"  # relative file path
file_path3 = "C:\\Users\\Ssara Gupta\\OneDrive\\Desktop\\test.txt"  # absolute path
file_path4 = "D:/Programming TICK/Python/Learn/youtube/stuff"

if os.path.exists(file_path1):
    print(f"The location {file_path1} exists")
else:
    print(f"{file_path1} doesn't exist")

if os.path.exists(file_path2):
    print(f"The location {file_path2} exists")
else:
    print(f"{file_path2} doesn't exist")

if os.path.exists(file_path3):
    print(f"The location {file_path3} exists")
else:
    print(f"{file_path3} doesn't exist")

if os.path.isfile(file_path2):
    print("This is file")
else:
    print("Not a file")

if os.path.isdir(file_path4):
    print("Directory")
else:
    print("Not")
