import datetime

billion = 1000000000

populationInOct2011 = 7 * billion
target = 8 * billion

current = populationInOct2011

currentYear = 2011

growthRate = 1.1 / 100
while target >= current:
    current += current * growthRate
    currentYear += 1

print(
    f"World population will be {int(target / billion)} billion in the year 2024.")

# PS D:\code\pystuff\assignment> python .\131-20-population-growth.py
# World population will be 8 billion in the year 2024.
