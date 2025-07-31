from typing import Tuple, List, Dict
from geopy.distance import geodesic


def closest_exit(
        user_location: Tuple[float, float],
        exits: List[Dict]
) -> Dict:
    """
    Finds the closest exit to the user's location

    Parameters:
        - user_location: (latitude, longitude) of user
        - exits: List of exit dictionaries

    Returns:
        The exit dictionary (element from the list) that is closest to user.
    """
    closest_exit = None
    shortest_distance = float("inf")

    for exit in exits:
        exit_coords = (exit["lat"], exit["lon"])
        distance = geodesic(user_location, exit_coords).meters

        if distance < shortest_distance:
            shortest_distance = distance
            closest_exit = exit.copy()
            closest_exit["distance"] = distance
    
    return closest_exit