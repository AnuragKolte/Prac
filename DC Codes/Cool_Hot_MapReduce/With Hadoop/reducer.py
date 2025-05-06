#!/usr/bin/env python3
import sys

year_temps = {}

for line in sys.stdin:
    try:
        year, temp = line.strip().split("\t")
        temp = float(temp)

        if year not in year_temps:
            year_temps[year] = {"min": temp, "max": temp}
        else:
            year_temps[year]["min"] = min(year_temps[year]["min"], temp)
            year_temps[year]["max"] = max(year_temps[year]["max"], temp)
    except ValueError:
        continue  # skip malformed lines

if not year_temps:
    print("No data to process.")
    sys.exit(1)

coolest_year = min(year_temps.items(), key=lambda x: x[1]["min"])
hottest_year = max(year_temps.items(), key=lambda x: x[1]["max"])

print(f"Coolest Year: {coolest_year[0]}, Min Temp: {coolest_year[1]['min']}")
print(f"Hottest Year: {hottest_year[0]}, Max Temp: {hottest_year[1]['max']}")