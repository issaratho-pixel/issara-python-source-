"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""

<<<<<<< HEAD
weight = float(input("Enter weight: (kg) "))
height = float(input("Enter height: (m) "))

BMI = weight / height ** 2

print("bmi_User = ", BMI)

if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI <= 24.9:
    print("Normal weight")
elif 25.0 <= BMI <= 29.9:
    print("Overweight")
else:
    print("Obese")
=======
>>>>>>> upstream/main

"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
<<<<<<< HEAD
"""

rate = 35.5

print("1. THAI BAHT (THB) to US DOLLARS (USD)")
print("2. US DOLLARS (USD) to THAI BAHT (THB)")

choice = input("Choose option: ")

if choice == "1":
    Amount = float(input("Enter amount in THB:"))
    USD = Amount / rate
    print(f"USD = {USD:.2f} USD") 

elif choice == "2":
    Amount = float(input("Enter amount in USD:"))
    THB = Amount * rate
    print(f"THB = {THB:.2f} THB") 
=======
"""
>>>>>>> upstream/main
