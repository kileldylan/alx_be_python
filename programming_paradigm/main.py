import sys
from bank_account import BankAccount

def main():
    # Initialize BankAccount with a default balance
    account = BankAccount(100)  # Example starting balance of Ksh 100

    # Check if the command-line arguments are sufficient
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit:<amount>, withdraw:<amount>, display")
        sys.exit(1)

    # Parse the command and amount from arguments
    try:
        command_input = sys.argv[1]
        if ":" in command_input:
            command, amount = command_input.split(":")
            amount = float(amount)  # Convert amount to a float
        else:
            command = command_input
            amount = None

        # Execute the appropriate command
        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: Ksh {amount:.2f}")
        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: Ksh {amount:.2f}")
        elif command == "display":
            account.display_balance()
        else:
            print("Invalid command. Use 'deposit:<amount>', 'withdraw:<amount>', or 'display'.")
    except ValueError:
        print("Invalid input. Amount must be a number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
