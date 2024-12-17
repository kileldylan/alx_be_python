def mad_libs():
    print("Hello, Welcome to Mad Libs. This is a game aimed to fill the blank spaces in the story below")
    
    #prompt the user to input desc
    day_variable = input("Enter adjective to describe the day ")
    animal1 = input("Enter adjective to describe the monkey ")
    animal2 = input("Enter adjective to describe the lion ")
    experience = input("Enter adjective to describe your experience ")
    
    #conditional statements
    if day_variable.lower() in ["rainy", "sunny", "windy"]:
        mood = "cheerul"
        activity = "was full of vibe"
    else:
        mood = "hyped"
        activity = "was full of energy and we played darts"
        
        # Build the Mad Libs story
    story = f"""
    On a {day_variable} day, I went to the zoo. The atmosphere was {mood}.
    I saw a funny {animal1} monkey swinging from the trees. 
    Then, I spotted a majestic {animal2} lion lounging in the sun. 
    The zoo {activity}, and it was a {experience} experience!
    """
    
    print("/n Here is your Mad Libs story")
    print(story)
    
    #run the program
mad_libs()
        

