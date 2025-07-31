# tbana-exit
**Determine the closest subway exit given an adress**

This code takes an address in Stockholm and returns the closes subway exit. The geocoding is done using [Nominatim](https://nominatim.org/) which uses data from OpenStreetMap to find the address location. The data file with data over all the subway station is sourced from https://github.com/mrkickling/rattuppgang-web


## How to use it

Run the program with `main.py` and enter an address when prompted. For example, entering "Roslagstullsbacken 21, Stockholm" will make the program output:
```
Station: Tekniska högskolan
Exit name: Valhallavägen/Körsbärsvägen
Distance: 857.5 meters
Direction: up
```
