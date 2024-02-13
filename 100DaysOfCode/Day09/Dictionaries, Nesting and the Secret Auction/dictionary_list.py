country = input("Enter the country: ")
visits = int(input("Enter the number of visits: "))
list_of_cities = input("Enter the list of cities (comma separated): ").split(', ')


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


def add_new_country(name, times_visited, cities_visited):
    new_country ={}
    new_country['country'] = name
    new_country['visits'] = times_visited
    new_country['cities'] = cities_visited

    travel_log.append(new_country)


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[-1]['country']} {travel_log[-1]['visits']} times")
print(f"My favourite city was {travel_log[-1]['cities'][0]}")