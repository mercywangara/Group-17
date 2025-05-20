
fun main() {
        val itinerary = Itinerary(destinations = emptyList(), travelDates = listOf("2025-06-01", "2025-06-02"))

        val nairobi = Destination(
            name = "Nairobi",
            travelTime = 120,
            activities = listOf("Visit Uhuru Gardens", "Explore Fort Jesus"),
            accommodations = "City Hotels"
        )

        val updatedItinerary = addDestination(itinerary, nairobi)

        println("Updated Itinerary: $updatedItinerary")
        println("Suggested Attractions in ${nairobi.name}: ${suggestAttractions(nairobi.name)}")
    }


data class Destination(
    val name: String,
    val travelTime: Int,
    val activities: List<String>,
    val accommodations: String
)

data class Itinerary(
    val destinations: List<Destination>,
    val travelDates: List<String>
)
fun addDestination(itinerary: Itinerary, destination: Destination): Itinerary {
    val updatedDestinations = itinerary.destinations.toMutableList()
    updatedDestinations.add(destination)
    return itinerary.copy(destinations = updatedDestinations)
}
fun suggestAttractions(destination: String): List<String> {
    val attractions = mapOf(
        "Nairobi" to listOf("Uhuru Gardens", "Fort Jesus Museum", "Karura Forest"),
        "New York" to listOf("Statue of Liberty", "Central Park", "Metropolitan Museum of Art")
    )
    return attractions[destination] ?: emptyList()
}