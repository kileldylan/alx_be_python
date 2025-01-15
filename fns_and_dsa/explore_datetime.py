from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    """Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format."""
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date and time
    print("Current Date and Time:", formatted_date)

# Part 2: Calculate a Future Date
def calculate_future_date():
    """Calculates and displays a future date based on user input."""
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))  # Get user input as integer
        current_date = datetime.now()  # Get the current date
        future_date = current_date + timedelta(days=days_to_add)  # Calculate the future date
        print("Future Date after adding", days_to_add, "days:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input! Please enter an integer value.")

# Main function to call the tasks
def main():
    display_current_datetime()  # Call the function to display current date and time
    calculate_future_date()  # Call the function to calculate and display a future date

if __name__ == "__main__":
    main()
