# Simple Travel Itinerary Planner

# Data structures
itinerary = []
attractions_db = {
    "Nairobi": ["Nairobi National Park", "Giraffe Centre", "Karen Blixen Museum"],
    "Mombasa": ["Fort Jesus", "Haller Park", "Nyali Beach"],
}
restaurants_db = {
    "Nairobi": ["Carnivore", "Talisman", "Java House"],
    "Mombasa": ["Tamarind", "Yul's", "Shehnai"],
}

# Function to add a destination
def add_destination():
    destination = input("Enter destination: ")
    travel_time = input("Estimated travel time (hours): ")
    activity = input("Main activity: ")
    preference = input("Any preference (nature, culture, food)? ")
    accommodation = input("Accommodation (hotel, hostel, Airbnb): ")
    dates = input("Travel dates (e.g., 2025-06-01 to 2025-06-05): ")
    stop = {
        "destination": destination,
        "travel_time": travel_time,
        "activity": activity,
        "preference": preference,
        "accommodation": accommodation,
        "dates": dates
    }
    itinerary.append(stop)
    print(f"{destination} added to your itinerary.")

# Function to suggest attractions and restaurants
def suggest(destination):
    print("\nSuggestions for", destination)
    print("Attractions:")
    for attr in attractions_db.get(destination, []):
        print("-", attr)
    print("Restaurants:")
    for rest in restaurants_db.get(destination, []):
        print("-", rest)

# Main loop
while True:
    print("\n1. Add Destination\n2. View Itinerary\n3. Get Suggestions\n4. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_destination()
    elif choice == "2":
        for stop in itinerary:
            print(stop)
    elif choice == "3":
        dest = input("Which destination do you want suggestions for? ")
        suggest(dest)
    elif choice == "4":
        break
    else:
        print("Invalid option.")