def get_trip_category(budget):
    if budget < 1000:
        return "Backpacker"
    elif budget < 3000:
        return "Standard"
    else:
        return "Luxury"

def get_travel_season(month):
    if month == "December":
        return "Peak Season"
    elif month == "June":
        return "Holiday Season"
    else:
        return "Regular Season"

def calculate_daily_budget(budget, days):
    return budget/days

def get_recommended_places(destination):
    if destination == "Japan":
        # A list holds multiple values
        recommended_places = [
        "Tokyo Tower",
        "Shibuya",
        "Mount Fuji"
        ]
    else:
        recommended_places = ["No recommendation available"]
    
    return recommended_places

def print_recommended_places(destination):
    print(f"Recommended Places")
    print()

    # Loop through the list
    for place in get_recommended_places(destination):
        print(f" - {place}")

        print()

    