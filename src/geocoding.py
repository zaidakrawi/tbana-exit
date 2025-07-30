# Code for adress to (lat, long) or (lat, long) to adress

from geopy.geocoders import Nominatim

def geocode(address: str) -> tuple[float, float]:
    geolocator = Nominatim(user_agent = "tbana-exit")
    location = geolocator.geocode("Kapellgränd 10, Stockholm")

    if location is True:
        print(f"Coordinates: ({location.latitude}, {location.longitude})")
        user_location = (location.latitude, location.longitude)    
    else:
        raise TypeError("Could not find the address.")
    
    return user_location


def haversin(user_location, exit_location):
    """
    Calculate the Haversin distance between the user location and location of the exit

    Parameters:
        - user_location: Lat and lon coordinates of user locaiton
        - exit_location: Lat and lon coordinates of exit

    Returns:
        - Distance of bird path from exit to user location
    """
    pass