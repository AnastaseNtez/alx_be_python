# temp_conversion_tool.py

FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def prompt_float(prompt_text):
    """
    Prompt the user and convert input to float.
    If conversion fails, raise the exact ValueError requested.
    """
    user_input = input(prompt_text)
    try:
        return float(user_input)
    except ValueError:
        # required error message when temperature is not numeric
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def main():
    try:
        temp = prompt_float("Enter the temperature to convert: ")
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted = convert_to_fahrenheit(temp)
            # show the original and converted temperatures
            print(f"{float(temp)}°C is {converted}°F")
        elif unit == 'F':
            converted = convert_to_celsius(temp)
            print(f"{float(temp)}°F is {converted}°C")
        else:
            # validate unit
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError as e:
        # friendly output for any validation error
        print(e)

if __name__ == "__main__":
    main()
