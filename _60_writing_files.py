# Python writing files (.txt, .json, .csv)

import csv
import json
from turtle import write

txt_data = "I like samosa!"
txt_data_append = "Hiya!!"

file_path = "C:\\Users\\Ssara Gupta\\OneDrive\\Desktop\\_60_1_output.txt"

employees = ["Anneliese", "Erika", "Rosella", "Odette", "Genevieve"]


with open(
    file_path, "w"
) as file:  # w to write a file # file is the name of File object
    file.write(txt_data)
    print(f"txt file '{file_path} was created'")


try:
    with open(file_path, "x") as file:  # exclusive create
        file.write(txt_data)
        print(f"txt file '{file_path} was created'")
except FileExistsError:
    print("File already exists!")

with open(file_path, "a") as file:  # exclusive create
    file.write("\n" + txt_data_append)
    print(f" txt file '{file_path} was appended'")

with open(file_path, "w") as file:
    for employee in employees:
        file.write(employee + "\n")
    print(f"txt file '{file_path} was created'")


# .json files

employee_json = {"name": "Genevive", "age": "23", "job": "Dancer"}

file_path_json = "C:\\Users\\Ssara Gupta\\OneDrive\\Desktop\\_60_2_output.json"

with open(file_path_json, "w") as file:
    json.dump(employee_json, file, indent=4)
    print(f"json file '{file_path_json} was created'")


# csv files common spread

employees_csv = [
    ["Name", "Age", "Job"],
    ["Lumine", 22, "Explorer"],
    ["Kaeya", 27, "Cavalry Captain"],
    ["Lisa", 26, "Librarian"],
    ["Xiangling", 20, "Chef"],
]

file_path_csv = "C:\\Users\\Ssara Gupta\\OneDrive\\Desktop\\_60_3_output.csv"

try:
    with open(file_path_csv, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees_csv:
            writer.writerow(row)
        print(f"csv file {file_path_csv} was created")
except FileExistsError:
    print("File already exists!")
