# Match case statement (switch): An alternative to using many elif statements, Execute same code if a value matches a 'case'
# Benifits: cleaner and syntax is more readable


def day_of_week(day):
    if day == 1:
        return "It's Sunday"
    elif day == 2:
        return "It's Monday"
    elif day == 3:
        return "It's Tuesday"
    elif day == 4:
        return "It's Wednesday"
    elif day == 5:
        return "It's Thursday"
    elif day == 6:
        return "It's Friday"
    elif day == 7:
        return "It's Saturday"
    else:
        return "Invalid day number! Please enter a number between 1 and 7."


day_input = int(input("Enter the number: "))
print(day_of_week(day_input))


def day_of_week_match_case(day):
    match day:
        case 1:
            return "It's Sunday"
        case 2:
            return "It's Monday"
        case 3:
            return "It's Tuesday"
        case 4:
            return "It's Wednesday"
        case 5:
            return "It's Thursday"
        case 6:
            return "It's Friday"
        case 7:
            return "It's Saturday"
        case _:
            return "Invalid day number! Please enter a number between 1 and 7."


day_input2 = int(input("Enter the number: "))
print(day_of_week_match_case(day_input2))


def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return "Invalid day!"


print(is_weekend("Sunday"))
