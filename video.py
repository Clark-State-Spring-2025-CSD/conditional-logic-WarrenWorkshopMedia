#Updated 1 Feb 2025
#Watch the video here: https://www.youtube.com/watch?v=YKxvDL3JxEA or follow the instructor led demo
#Implement all the code shown in the video.
#Modify the code so the checks from 12 and under for the $8 price tag
#and 62 and older for the $9 price tag.

print("Welcome to the Menu Ordering System")

CustomerAge = int(input("What is the age of the customer? "))

price = 0

if CustomerAge <= 12:
    price = 8
elif CustomerAge >= 62:
    price = 9
else:
    price = 12

print(f"the cost for this customer is ${price}.")

drinkYesNo = input("Add a drink? Y/N? ")

if drinkYesNo == "Y" or drinkYesNo == "y":
    SmallLarge = input("Small or Large? S/L? ")
    if SmallLarge == "L":
        price += 2
    else:
        price += 1

print(f"Total is: ${price}.")


