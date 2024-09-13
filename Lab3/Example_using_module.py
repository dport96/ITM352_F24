import temperature_conversions as tc
from temperature_conversions import celsius_to_fahrenheit, fahrenheit_to_celsius, fahrenheit_to_kelvin, max


# Example temps
celsius_temp = 25
fahrenheit_temp = 77

# Convert temps

print(f"{celsius_temp}°C is { tc.celsius_to_fahrenheit(celsius_temp)}°F")

print(f"{fahrenheit_temp}°F is { tc.fahrenheit_to_celsius(fahrenheit_temp)}°C")

print(f"{fahrenheit_temp}°F is { tc.fahrenheit_to_kelvin(fahrenheit_temp)}°K")

print(f"Max of 5 and 10 is {max(5,10)}")