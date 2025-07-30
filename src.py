import json

# open and read json file
with open("data.json", "r", ) as file:
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
            # lat_str, lon_str = exit_info['pos'].split(",")
            # lat = float(lat_str)
            # lon = float(lon_str)

            pos = exit_info.get("pos")
            if not pos:
                continue  # skip this exit if it doesn't have coordinates

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


print(f"Extracted {len(all_exits)} exits.")
print("First 3 exits:")
for exit in all_exits[:3]:
    print(exit)