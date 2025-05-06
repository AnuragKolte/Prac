#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue  # Skip empty lines

    parts = line.split(",")
    if len(parts) < 3:
        continue  # Malformed line

    date = parts[1]
    year = date.split("-")[0]

    try:
        temperature = float(parts[2])
        print(f"{year}\t{temperature}")
    except ValueError:
        continue  # Skip lines with invalid temperature