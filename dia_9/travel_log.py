travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

def add_new_country(country, visits, cities ):
    """Function the adds a new country in the dictionary above"""
    new_travel_log = {}
    cities = []
    country = input("Insert a country: ")
    cities = input("Insert the name of the cities, separed by ',': ").split(",")
    visits = len(cities)

    new_travel_log = {
        "country": country,
        "visitis": visits,
        "cities": cities
    } 
    travel_log.append(new_travel_log)
#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
