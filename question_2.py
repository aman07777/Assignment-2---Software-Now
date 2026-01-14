"""Question 2
Create a program that analyses temperature data collected from multiple weather
stations in Australia. The data is stored in multiple CSV files under a "temperatures"
folder, with each file representing data from one year. Process ALL .csv files in the
temperatures folder. Ignore missing temperature values (NaN) in calculations.
Main Functions to Implement:
Seasonal Average: Calculate the average temperature for each season across ALL
stations and ALL years. Save the results to "average_temp.txt".
• Use Australian seasons: Summer (Dec-Feb), Autumn (Mar-May), Winter (JunAug), Spring (Sep-Nov)
• Output format example: "Summer: 28.5°C"
Temperature Range: Find the station(s) with the largest temperature range (difference
between the highest and lowest temperature ever recorded at that station). Save the
results to "largest_temp_range_station.txt".
• Output format example: "Station ABC: Range 45.2°C (Max: 48.3°C, Min: 3.1°C)"
• If multiple stations tie, list all of them
Temperature Stability: Find which station(s) have the most stable temperatures
(smallest standard deviation) and which have the most variable temperatures (largest
standard deviation). Save the results to "temperature_stability_stations.txt".
• Output format example:
o "Most Stable: Station XYZ: StdDev 2.3°C"
o "Most Variable: Station DEF: StdDev 12.8°C"
• If multiple stations tie, list all of them"""



import csv
import glob
import math


# it read all CSV files 
files = glob.glob("temperatures/*.csv")

# it just map month column names to the season they belong to 
season_map = {
    "December": "Summer", "January": "Summer", "February": "Summer",
    "March": "Autumn", "April": "Autumn", "May": "Autumn",
    "June": "Winter", "July": "Winter", "August": "Winter",
    "September": "Spring", "October": "Spring", "November": "Spring"
}

# Containers for temperatures
season_temperatures = {"Summer": [], "Autumn": [], "Winter": [], "Spring": []}
station_temperatures = {}


for file in files:
    with open(file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            station = row["STATION_NAME"]
            if station not in station_temperatures:
                station_temperatures[station] = []

            for month, season in season_map.items():
                val = row.get(month, "")
                if val != "":
                    temp = float(val)
                    season_temperatures[season].append(temp)
                    station_temperatures[station].append(temp)

# here we simply average all temperatures collected for each season
with open("average_temperature.txt", "w") as f:
    for season in ["Summer", "Autumn", "Winter", "Spring"]:
        temps = season_temperatures[season]
        avg = sum(temps) / len(temps) if temps else 0
        f.write(f"{season}: {avg:.1f}°C\n")


# here for each station we record max and min across all months years
max_range = 0
ranges = {}
for station, temps in station_temperatures.items():
    if temps:
        r = max(temps) - min(temps)
        ranges[station] = (r, max(temps), min(temps))
        if r > max_range:
            max_range = r

with open("largest_temperature_range_station.txt", "w") as f:
    for station, (r, mx, mn) in ranges.items():
        if r == max_range:
            f.write(f"station {station}: range {r:.1f}C (max: {mx:.1f}C, min: {mn:.1f}C)\n")


# here we compute the population standard deviation  for each station ties are handled
# by checking equality against the min max values and writing all matches.
stds = {}
for station, temps in station_temperatures.items():
    if temps:
        mean_val = sum(temps) / len(temps)
        variance = sum((t - mean_val)**2 for t in temps) / len(temps)
        stds[station] = math.sqrt(variance)

minumu_std = min(stds.values())
maximum_std = max(stds.values())

with open("temperature_stability_stations.txt", "w") as f:
    for station, sd in stds.items():
        if sd == minumu_std:
            f.write(f"most stable: station {station}: StdDev {sd:.1f}C\n")
    for station, sd in stds.items():
        if sd == maximum_std:
            f.write(f"most variable: station {station}: StdDev {sd:.1f}C\n")



 
 