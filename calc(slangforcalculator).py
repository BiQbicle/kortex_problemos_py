value = float(input("Enter the value: "))
direction = input("do you wanna convert to (miles/km or celsius/fahrenheit): ").lower()

if direction == "miles":
    result = value * 0.621371
    print(f"{value} km is {result:.2f} miles, morales")
elif direction == "km":
    result = value / 0.621371
    print(f"{value} miles is {result:.2f} km")
elif direction == "fahrenheit":
    result = (value * 9/5) + 32
    print(f"{value}°C is {result:.2f}°F")
elif direction == "celsius":
    result = (value - 32) * 5/9
    print(f"{value}°F is {result:.2f}°C")
else:
    print("You retard choose the right options")