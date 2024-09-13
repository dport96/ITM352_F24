# temperature_conversions.py

def convert_temperature(value, conversion_func):
    """Converts temperature using the provided conversion function."""
    return f"{conversion_func.__name__} {value} is {conversion_func(value)}"

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    return (fahrenheit - 32) * 5/9 + 273.15

def max(x,y):
    return 999