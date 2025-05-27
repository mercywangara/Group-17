
def travel_itineraries(destination, estimated_travel_times, activities, preferences, accomodations):
    attractions = [{"Uganda":["Mt.Rwenzori", "L.Victoria"]}, {"Rwanda":["Gorillas", "L.Kivu"]}]
    restaurants = [{"Uganda": ["Serena", "Sheraton"]}, {"Rwanda":["Hornbill", "Calvary"]}]
    for attraction in attractions:
        if destination==attractions[destination]:
            print(f"Consider the following reccommendations: {attraction[destination]}")
        else:
            print("We have no reccommendations")
    for restaurant in restaurants:
        if destination==restaurants[destination]:
            print(f"Consider the following reccommendations: {restaurants[destination]}")
        else:
            print("We have no reccommendations")
    