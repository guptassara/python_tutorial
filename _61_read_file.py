# python reading files (.txt, .json, .csv)
import csv
import json

file_path_txt = "C:\\Users\\Ssara Gupta\\OneDrive\\Desktop\\_60_1_output.txt"
try:
    with open(file_path_txt, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("No permission")

# json
# "C:\Users\Ssara Gupta\OneDrive\Desktop\_60_2_output.json"
file_path_json = "C:\\Users\\Ssara Gupta\\OneDrive\\Desktop\\_60_2_output.json"
try:
    with open(file_path_json, "r") as file:
        content = json.load(file)
        print(content)
        print(f"Name is {content['name']}")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("No permission")


# csv "C:\Users\Ssara Gupta\OneDrive\Desktop\_60_3_output.csv"
file_path_csv = "C:\\Users\\Ssara Gupta\\OneDrive\\Desktop\\_60_3_output.csv"
try:
    with open(file_path_csv, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
            print(f"job are: {line[2]}")
        # print(content)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("No permission")
