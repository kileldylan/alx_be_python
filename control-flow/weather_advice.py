def weather_advices():
    print("Welcome to this weather advice program")
    
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()
    
    if weather == "sunny":
        print("Wear a T-shirt and sunglasses ")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf")
    else:
        print("Sorry, I don't have recommendations for this weather")
        
weather_advices()