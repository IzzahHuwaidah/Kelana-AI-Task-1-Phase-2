from services.trip_service import (
    get_trip_category, 
    get_travel_season, 
    calculate_daily_budget, 
    print_recommended_places
)

# Variables store the trip data
destination = input("destination : ")
country = input("Country : ")
days = int(input("Days : "))
budget = float(input("Budget : "))
currency = input("Currency : ")
travel_month = input("Travel Month : ")

season = get_travel_season(travel_month)
category = get_trip_category(budget)
daily_budget = calculate_daily_budget(budget, days)

# Functions 
def print_trip_summary(destination, days, budget, currency, category, daily_budget, travel_month, season):
    print("========================")
    print("KelanaAI")
    print("========================")
    print(f"Destination     : {destination}")
    print(f"Days            : {days}")
    print(f"Budget          : {budget} {currency}")
    print(f"Category        : {category}")
    print(f"Daily Budget    : {daily_budget} {currency}/Day")
    print(f"Travel Month    : {travel_month}")
    print(f"Season          : {season}\n")
    print_recommended_places(destination)

# Call it with any trip
print_trip_summary(destination, days, budget, currency, category, daily_budget, travel_month, season)

