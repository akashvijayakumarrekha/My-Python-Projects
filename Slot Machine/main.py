import random

# Maximum number of lines, maximum and minimum bets
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Number of rows and columns in the slot machine grid
ROWS = 3
COLS = 3

# Dictionary of symbol counts for each symbol
symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}

# Dictionary of symbol values for each symbol
symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}


def check_winnings(columns, lines, bet, values):
    """
    Calculate winnings and winning lines based on the provided columns,
    number of lines, bet amount, and symbol values.

    Args:
        columns (list): List of lists representing the slot machine grid.
        lines (int): Number of lines the player is betting on.
        bet (int): Bet amount for each line.
        values (dict): Dictionary containing symbol values.

    Returns:
        tuple: A tuple containing total winnings and a list of winning lines.
    """
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines


def get_slot_machine_spin(rows, cols, symbols):
    """
    Generate a slot machine grid with random symbol combinations.

    Args:
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.
        symbols (dict): Dictionary containing symbol counts.

    Returns:
        list: A list of lists representing the slot machine grid.
    """
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []

    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    """
    Print the slot machine grid.

    Args:
        columns (list): List of lists representing the slot machine grid.
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" | ")
        print()


def deposit():
    """
    Prompt the user for a deposit amount.

    Returns:
        int: The deposit amount.
    """
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


# ... (previous functions)


def get_number_of_lines():
    """
    Prompt the user for the number of lines they want to bet on.

    Returns:
        int: The number of lines to bet on.
    """
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
    """
    Prompt the user for the bet amount for each line.

    Returns:
        int: The bet amount for each line.
    """
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


def spin(balance):
    """
    Execute a single round of the slot machine game.

    Args:
        balance (int): The player's current balance.

    Returns:
        int: The difference between the winnings and the total bet.
    """
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

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)

    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, line, bet, symbol_value)
    print(f"You won €{winnings}.")
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet


def main():
    """
    The main game loop that orchestrates the entire slot machine game.
    """
    balance = deposit()
    while True:
        print(f"Current balance is €{balance}")
        answer = input("Press Enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You are left with €{balance}")


if __name__ == "__main__":
    main()
