def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit_to_celsius(fahrenheit)) + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def main():
    # Get the temperature value from the user
    temp_value = float(input("Enter the temperature value: "))
    
    # Get the temperature unit from the user
    temp_unit = input("Enter the temperature unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()
    
    if temp_unit == 'K':
        # Convert Kelvin to Celsius and Fahrenheit
        celsius = kelvin_to_celsius(temp_value)
        fahrenheit = kelvin_to_fahrenheit(temp_value)
        print(f"Temperature in Celsius: {celsius:.2f}°C")
        print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")
    elif temp_unit == 'C':
        # Convert Celsius to Fahrenheit and Kelvin
        fahrenheit = celsius_to_fahrenheit(temp_value)
        kelvin = celsius_to_kelvin(temp_value)
        print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")
        print(f"Temperature in Kelvin: {kelvin:.2f}K")
    elif temp_unit == 'F':
        # Convert Fahrenheit to Celsius and Kelvin
        celsius = fahrenheit_to_celsius(temp_value)
        kelvin = fahrenheit_to_kelvin(temp_value)
        print(f"Temperature in Celsius: {celsius:.2f}°C")
        print(f"Temperature in Kelvin: {kelvin:.2f}K")
    else:
        print("Invalid temperature unit. Please enter 'C', 'F', or 'K'.")

if __name__ == "__main__":
    main()
