# membership operators: used to test whether a value or variable is found in a sequence (string, list, tuple, set or dictionary)
# 1. in
# 2. not in

# STRING
word = "apple"
letter = input("Guess a letter in the word: ")
if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

word2 = "mango"
if letter not in word2:
    print(f"{letter} was not found")
else:
    print(f"{letter} was found")


# SET
students = {"mavuika", "clorinde", "wriothesely", "nefer"}
student = input("Enter the name of student: ").lower()

if student in students:
    print(f"{student} was found")
else:
    print(f"{student} was not found")

# DICTIONARIS
grades = {"Mavuika": "A", "Sucrose": "B", "Ororon": "C", "Itto": "D"}

student_dict = input("Enter the name of student: ").capitalize()
if student_dict in grades:
    print(f"{student_dict}'s grade is {grades[student_dict]}")
else:
    print(f"{student_dict} was not found")


# string
email = input("Enter your email: ")
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")
