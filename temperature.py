print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2): "))
temp = float(input("Enter temperature: "))

if choice == 1:
    fahrenheit = (temp * 9 / 5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

elif choice == 2:
    celsius = (temp - 32) * 5 / 9
    print("Temperature in Celsius:", celsius)

else:
    print("Invalid choice")
