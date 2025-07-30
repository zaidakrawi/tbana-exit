import json

def load_exits(filepath):
    """
    Loads and flattens all Tunnelbana exits from the data file

    Parameters:
        - filepath: Path to data.json file

    Returns:
        - List of flattened exit dictionaries in the format
            flat_exit = {
                    "station": station_name,
                    "exit_name": exit_name),
                    "lat": lat,
                    "lon": lon,
                    "elevator": elevator_info,
                    "direction": direction
                }
    """
    # open and read json file
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)


    ## flatten the exits and put them into a list
    all_exits = []


    for station_name, station_info in data.items():
        exit_direction = station_info.get("exits", {})

        # loop through each direction
        for direction in ["up", "middle", "down"]:
            exits = exit_direction.get(direction, [])

            #loop through each exit in that direction
            for exit_info in exits:
                pos = exit_info.get("pos")
                if not pos:
                    continue  # skip exit if no coords found

                try:
                    lat_str, lon_str = pos.split(",")
                    lat = float(lat_str)
                    lon = float(lon_str)
                except ValueError:
                    continue  # skip malformed coordinates

                #create flat exit dict
                flat_exit = {
                    "station": station_name,
                    "exit_name": exit_info.get("name", "Unnamed exit"),
                    "lat": lat,
                    "lon": lon,
                    "elevator": exit_info.get("elevator", False),
                    "direction": direction
                }

                all_exits.append(flat_exit)

    return all_exits