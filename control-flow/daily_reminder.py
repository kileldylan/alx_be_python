#pyhton script used to create a daily reminder program

def daily_reminder():
    #prompt the user to input the task description, level of priority and if it is time bound
    print("Welcome to your daily reminder")
    task = input("Enter your task: ")
    Is_it_timebound =input("Is it time-bound (yes/no)").lower()
    priority = input("Priority (high/medium/low)").lower()

    match task:
        case _ if priority == "high" and Is_it_timebound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        case _ if priority == "medium" and Is_it_timebound == "yes":
            print(f"Reminder: {task} is a medium priority task that doesn't require immediate attention!")
        case _ if priority == "low" and Is_it_timebound == "no":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.!")

daily_reminder()

