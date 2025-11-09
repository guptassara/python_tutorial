# 1. Show balance
# 2. Deposit
# 3. Withdraw


def show_balance(balance: float):
    if balance == 0:
        print("⚠️  No money deposited")
    else:
        print(f"\n💰 Your current balance is: ₹ {balance:,.2f}")


def deposit():
    amount = float(input("Enter an amount to be deposited:"))

    if amount > 0:
        print(f"✅  Successfully deposited ₹ {amount:,.2f}")
        return amount
    else:
        print("  ❎Invalid amount")
        return 0


def withdraw(balance: float):
    amount = float(input("Enter amount to withdraw"))
    if amount > balance:
        print("⚠️  Insufficient balance!")
        return 0
    elif amount > 0:
        print(f"💸 Successfully withdrew ₹{amount:,.2f}")
        return amount
    else:
        print("❎  Invalid amount")
        return 0


def main():
    balance = 0.00
    is_running = True

    while is_running:
        print("\n" + "═" * 40)
        print("💸  BANKING PROGRAM  💸".center(40))
        print("═" * 40)
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("═" * 40)

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("❎Invalid choice! Please select between 1–4.")

    print("\n🌸 Thank you for using our bank! Have a wonderful day! 🌸\n")


if __name__ == "__main__":
    main()
