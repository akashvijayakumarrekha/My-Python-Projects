import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3


def deposit():
    while True:
        amount = input("How much would you like to deposit? €")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The deposit amount must be greater than 0.")

        else:
            print("Please enter a valid amount.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? "
        )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")

        else:
            print("Please enter a valid number of lines")

    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? €")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}.")

        else:
            print("Please enter a valid amount.")

    return amount


def main():
    balance = deposit()
    line = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = line * bet
        if total_bet >= balance:
            print(
                f"You do not have sufficient funds to bet that amount. Your current balance is €{balance}"
            )
        else:
            break

    print(f"Your are betting €{bet} on {line} lines. Total bet is: €{total_bet}")


main()
