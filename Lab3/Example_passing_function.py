import temperature_conversions as tc

# Example temps
celsius_temp = 25
fahrenheit_temp = 77

# Convert temps

print(f"{celsius_temp}°C is { tc.convert_temperature(celsius_temp, tc.celsius_to_fahrenheit)}°F")

print(f"{fahrenheit_temp}°F is { tc.convert_temperature(fahrenheit_temp, tc.fahrenheit_to_celsius)}°C")

print(f"{fahrenheit_temp}°F is { tc.convert_temperature(fahrenheit_temp, tc.fahrenheit_to_kelvin)}°K")