# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:33:59 2024

@author: Regan
"""

def convert_and_display(temperature, original_unit):
    # Convert to Celsius for calculation
    if original_unit == 'F':
        celsius = (temperature - 32) * 5 / 9
    elif original_unit == 'K':
        celsius = temperature - 273.15
    else:
        celsius = temperature

    # Convert to Fahrenheit
    fahrenheit = (celsius * 9 / 5) + 32

    # Convert to Kelvin
    kelvin = celsius + 273.15

    # Display results
    print("Converted Temperatures:")
    print(f"Celsius: {celsius}")
    print(f"Fahrenheit: {fahrenheit}")
    print(f"Kelvin: {kelvin}")

# Prompt user for input
temperature = float(input("Enter temperature value: "))
original_unit = input("Enter original unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

# Convert temperature and display results
convert_and_display(temperature, original_unit)
