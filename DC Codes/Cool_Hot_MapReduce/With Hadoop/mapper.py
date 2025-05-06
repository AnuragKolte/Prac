#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if line.startswith("dt") or not line:
        continue  # skip header or empty lines

    parts = line.split(",")
    if len(parts) < 2:
        continue  # skip malformed lines

    date = parts[0]
    year = date.split("-")[0]

    try:
        temperature = float(parts[1])
        print(f"{year}\t{temperature}")
    except ValueError:
        continue  # skip lines with invalid temperature