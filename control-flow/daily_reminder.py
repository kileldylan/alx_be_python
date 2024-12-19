def daily_reminder():
    # Prompt the user to input the task description, level of priority, and if it is time-bound
    print("Welcome to your daily reminder")
    task = input("Enter your Task: ")  # Adjusted prompt
    time_bound = input("Is it time-bound (yes/no): ").lower()  # Adjusted prompt and naming
    priority = input("Priority (high/medium/low): ").lower()  # Adjusted prompt and naming

    # Match Case statement for basic conditions
    match (priority, time_bound):
        case ("high", "yes"):
            print(f"Reminder: {task} is a high-priority task that requires immediate attention today!")
        case ("medium", "yes"):
            print(f"Reminder: {task} is a medium-priority task. Address it soon.")
        case ("low", "no"):
            print(f"Note: {task} is a low-priority task. Consider completing it when you have free time.")
        case _:
            print(f"Task: {task} doesn't match predefined conditions. Please review your inputs.")

    # Additional customization using `if`
    if time_bound == "yes" and priority == "high":
        print(f"Action Required: {task} must be completed immediately due to its high priority.")

# Call the function
daily_reminder()
