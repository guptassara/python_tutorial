import random


def spin_row():
    symbols = ["🍒", "🍉", "🔔", "⭐"]

    # results = []
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    #
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print("\n" + "═" * 40)
    print("|".join(row))
    print("\n" + "═" * 40)


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 1
        elif row[0] == "🍉":
            return bet * 2
        elif row[0] == "🔔":
            return bet * 3
        elif row[0] == "⭐":
            return bet * 4
        else:
            return 0
    else:
        return 0


def main():
    balance = 100.00
    print("\n" + "═" * 40)
    print("🎰  WELCOME TO PYTHON SLOTS  🎰".center(40))
    print("\n" + "═" * 40)

    while balance > 0:
        print(f"Current balance: ₹{balance}")
        bet = input("Enter your bet amount:")
        if not bet.isdigit():
            print("Invalid")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than zero")
            continue

        balance -= bet

        row = spin_row()  # list
        print("\nSpinning!!")
        print_row(row)
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ₹{payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to play again? (y/n)?:").lower()

        if play_again != "y":
            break
    print("\n" + "═" * 40)
    print(f"Game over!! Your final balance is ₹{balance}")
    print("\n" + "═" * 40)
    print("Thank you for playing!!")


if __name__ == "__main__":
    main()
