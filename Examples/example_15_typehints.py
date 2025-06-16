"""Make use of type hints for warnings and code completion in your IDE"""
import requests


from typing import List, Tuple

from requests import Response

URL = "https://nominatim.openstreetmap.org/reverse"

Coordinates = Tuple[float, float]


# Function type annotations
def get_location_name(coords: Coordinates) -> tuple:
    params = {'lat': coords[0], 'lon': coords[1], 'format': 'json', 'zoom': 12}
    response: Response = requests.get(URL, params)
    response.raise_for_status()
    location_details: dict = response.json()
    address: dict = location_details['address']
    return ((address.get('city') or address.get('town')), address['state'], address['country'])


# Variable with builtin types
vancouver: tuple = (45.63, -122.67)
dublin: tuple[float, float] = (40.10, -83.11)

print(get_location_name(vancouver))  # PyCharm shows type mismatch because tuple != tuple[float, float]

# Using types from typing module
london: Tuple[float, float] = (42.99, -81.25)
cities: List[Tuple[float, float]] = [vancouver, dublin]

# Using type aliases (Coordinates defined at top of file)
brooklyn: Coordinates = (-37.816, 144.842)
more_cities: List[Coordinates]
more_cities = [dublin, london, brooklyn]

for city in more_cities:
    print(get_location_name(city))

# Can define type before assignment
a: str

try:
    # Check if your IDE supports annotation code suggestions
    a.upper()
except Exception as e:
    print(repr(e))
# print(__annotations__)