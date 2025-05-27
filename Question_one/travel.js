const attraction = {
  "Nairobi": ["Nairobi National Park", "Giraffe Centre", "Karen Blixen Museum"],
  "Mombasa": ["Fort Jesus", "Haller Park", "Nyali Beach"],
  "Kampala": ["Kasubi Tombs", "Uganda Museum", "Lake Victoria"],
};

const restaurant = {
  "Nairobi": ["Carnivore", "Talisman", "Java House"],
  "Mombasa": ["Tamarind", "Yul's", "Shehnai"],
  "Kampala": ["Cafe Javas", "The Lawns", "Fang Fang"],
};


const itinerary = [];

function addDestination({ destination, travelTime, activities, preferences, accommodation, dates }) {
  itinerary.push({
    destination,
    travelTime,
    activities,
    preferences,
    accommodation,
    dates
  });
  console.log(`${destination} added to your itinerary.`)
}

function suggest(destination) {
  const attractions = attraction[destination];
  const restaurants = restaurant[destination] ;
  console.log(`Suggestions for ${destination}:`);
  console.log("  Attractions:");
  if (attractions.length) {
    return attractions.map(attr => console.log(` ${attr}`));
  } else {
    console.log("No suggestions available");
  }
  console.log("  Restaurants:");
  if (restaurants.length) {
    restaurants.map(rest => console.log(` ${rest}`));
  } else {
    console.log("No suggestions available")
  }
}


addDestination({
  destination: "Nairobi",
  travelTime: 6,
  activities: ["Safari", "Culture"],
  preferences: ["Nature", "Wildlife"],
  accommodation: "Hotel",
  dates: "2025-06-01 to 2025-06-05"
});

addDestination({
  destination: "Mombasa",
  travelTime: 8,
  activities: ["Beach", "History"],
  preferences: ["Relaxation", "Exploration"],
  accommodation: "Resort",
  dates: "2025-06-06 to 2025-06-10"
});
suggest("Nairobi");
suggest("Mombasa");
