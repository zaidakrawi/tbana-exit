# Code for adress to (lat, long) or (lat, long) to adress

from geopy.geocoders import Nominatim # type: ignore
# import numpy as np

# define once
geolocator = Nominatim(user_agent = "tbana-exit")

def geocode(address: str) -> tuple[float, float]:
    """
    Geocodes input address to (latitude, longitude)
    # """
    # location = geolocator.geocode("Kapellgränd 10, Stockholm")
    location = geolocator.geocode(address)

    if location is not None:
        return (location.latitude, location.longitude)
    else:
        raise ValueError(f"Could not geocode address: {address}")

    # if location is True:
    #     print(f"Coordinates: ({location.latitude}, {location.longitude})")
    #     user_location = (location.latitude, location.longitude)    
    # else:
    #     raise TypeError("Could not find the address.")
    
    # return user_location



def haversin(user_location, exit_location):
    """
    Calculate the Haversin distance (as-the-crow-flies) between the user location and location of the exit

    Parameters:
        - user_location: Lat and lon coordinates of user locaiton
        - exit_location: Lat and lon coordinates of exit

    Returns:
        - Distance of bird path from exit to user location
    """
    # R = 6371e3     # radius of earth

    # dphi = (exit_location[0] - user_location[0])*np.pi/180.0
    # dlambda = (exit_location[1] - user_location[1])*np.pi/180.0

    # phi1 = user_location[0]*np.pi/180.0
    # phi2 = exit_location[0]*np.pi/180.0

    # a = np.sin(dphi/2)**2 + np.cos(phi1)*np.cos(phi2)*(np.sin(dlambda/2)**2)
    # c = 2*np.arctan2(np.sqrt(a), np.sqrt(1-a))

    # return R*c
