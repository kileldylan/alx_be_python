import sys
from bank_account import BankAccount

def main():
    account = BankAccount(250)  # Initial balance of $250 for the example

    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit:<amount>, withdraw:<amount>, display")
        sys.exit(1)

    command_input = sys.argv[1]
    if ":" in command_input:
        command, amount = command_input.split(":")
        amount = float(amount)
    else:
        command = command_input
        amount = None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")  # Print only in main
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Use 'deposit:<amount>', 'withdraw:<amount>', or 'display'.")

if __name__ == "__main__":
    main()
