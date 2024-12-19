#pyhton script used to create a daily reminder program

def daily_reminder():
    #prompt the user to input the task description, level of priority and if it is time bound
    print("Welcome to your daily reminder")
    Task = input("Enter your task: ")
    Time_Bound =input("Is it time-bound (yes/no)").lower()
    Priority = input("Priority (high/medium/low)").lower()

    match Task:
        case _ if Priority == "high" and Time_Bound == "yes":
            print(f"Reminder: {Task} is a high priority task that requires immediate attention today!")
        case _ if Priority == "medium" and Time_Bound == "yes":
            print(f"Reminder: {Task} is a medium priority task that doesn't require immediate attention!")
        case _ if Priority == "low" and Time_Bound == "no":
            print(f"Note: {Task} is a low priority task. Consider completing it when you have free time.!")

daily_reminder()

