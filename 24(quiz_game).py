questions = (
    "What is a tuple in Python and how is it different from a list?",
    "How do you create an empty tuple?",
    "Can a tuple contain elements of different data types?",
    "What happens if you try to modify an element inside a tuple?",
    "How can you access the third element in a tuple named 'my_tuple'?",
)
options = (
    (
        "A. A tuple is an immutable sequence, unlike lists which are mutable",
        "B. Tuples are defined using curly braces",
        "C. Lists take less memory than tuples",
        "D. Tuples can only contain strings",
    ),
    (
        "A. Using empty square brackets []",
        "B. Using empty curly braces {}",
        "C. Using tuple()",
        "D. Using empty parentheses ()",
    ),
    (
        "A. No, all elements must be of the same type",
        "B. Yes, tuples can store mixed data types",
        "C. Only strings and integers are allowed",
        "D. Only lists are allowed in tuples",
    ),
    (
        "A. It throws an error because tuples are immutable",
        "B. It updates the tuple",
        "C. It deletes the element automatically",
        "D. It replaces the element with None",
    ),
    ("A. my_tuple[3]", "B. my_tuple(2)", "C. my_tuple[2]", "D. my_tuple.get(2)"),
)

answers = ("A", "D", "B", "A", "C")

guesses = []  # we will append guesses so list
score = 0
question_num = 0

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("✧･ﾟ: *✧･ﾟ:* 　 *:･ﾟ✧*:･ﾟ✧")
print("        RESULTS        ")
print("✧･ﾟ: *✧･ﾟ:* 　 *:･ﾟ✧*:･ﾟ✧")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
