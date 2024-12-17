def weather_advices():
    print("Welcome to this weather advice program")
    
    # Prompt user for the weather
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()
    
    # Check weather conditions and provide advice
    if weather == "sunny":
        print("Wear a T-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

# Call the function
weather_advices()
