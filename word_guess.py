import random

number_list = ["fire", "banana", "nigga"]
selected_number = random.choice(number_list)
print(selected_number)

while True:
 choice_number = str(input("choose zhe wortd vro: "))
 if choice_number == selected_number:
    print("dayum ur good")
    break
    
 elif choice_number != selected_number:
     print("try again nga: ")     


    