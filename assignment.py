#Updated 1 Feb 2025
#Create a program that will ask the user for a number between 1 and 12. You may assume the input is correct.
#After getting the number display which season it is. The ranges are:
#Spring: 3,4,5
#Summer: 6,7,8
#Fall: 9,10,11
#Winter 12,1,2
#Here is a sample output:
#What month is it? (1-12): 2
#The current season is Winter.
#For an extra 2 points, display the month as all. So the output becomes:
#What month is it? (1-12): 2
#The month is February and the current season is Winter.
#Remember to also complete the flowchart. It is strongly advised that you do the flowchart first,
#as this will help you write the code.

MonthNumber = int(input("Enter a number representing a month: "))

if MonthNumber in [12, 1, 2]:
    season = "Winter"
    if MonthNumber in {12}:
        month = "December"
    elif MonthNumber in {1}:
        month = "January"
    elif MonthNumber in {2}:
        month = "February"
elif MonthNumber in [3, 4, 5]:
    season = "Spring"
    if MonthNumber in {3}:
        month = "March"
    elif MonthNumber in {4}:
        month = "April"
    elif MonthNumber in {5}:
        month = "May"
elif MonthNumber in [6, 7, 8]:
    season = "Summer"
    if MonthNumber in {6}:
        month = "June"
    elif MonthNumber in {7}:
        month = "July"
    elif MonthNumber in {8}:
        month = "August"
elif MonthNumber in [9, 10, 11]:
    season = "Fall"
    if MonthNumber in {9}:
        month = "September"
    elif MonthNumber in {10}:
        month = "October"
    elif MonthNumber in {11}:
        month = "November"

print(f"The month is {month} and the current season is {season}.")


