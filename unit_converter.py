initial_tobeconverted = float(input("Enter an initial value you want to convert: "))
print("1. M - CM")
print("2. Farenheit - Celsius")
print("3. Miles - Km")
print("4. Nigerian Monkeys - Goons per second")
choice = int(input("Enter the value you want to convert: "))
if choice == 1:
    sum = initial_tobeconverted * 100
    print("Your Answer is: {}", sum)
    
elif choice == 2:
    sum = (initial_tobeconverted - 30) / 2
    print("Your answer is: {}", sum)
    
elif choice == 3:
    sum = initial_tobeconverted * 1.609
    print("Your answer is: {}", sum)
elif choice == 4:
    sum = initial_tobeconverted * 100000000 / 2 * 1 / 1 / 1
    print("Your answer is: {}", sum)

