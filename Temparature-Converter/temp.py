unit = input("Temperature in Fahrenheit or Celsius (C/F): ").strip().upper()

try:
    temp = float(input("Enter The Temperature: "))
except ValueError:
    print("Error: Please enter a valid number for temperature.")
    exit()

if unit == "C":
    temp_f = round((9 * temp) / 5 + 32, 1)
    print(f"The Temperature in Fahrenheit is: {temp_f}°F")

elif unit == "F":
    temp_c = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp_c}°C")

else:
    print(f"{unit} is an invalid unit of measurement. Please enter C or F.")