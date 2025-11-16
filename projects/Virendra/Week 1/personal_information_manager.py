"""
Project 1: Personal Information Manager (Beginner)
Description: Create a CLI program that collects and displays user information with formatted output.
Requirements:

Collect user's name, age, email, and city
Validate age (must be a number, between 0-120)
Check if email contains '@' symbol
Display formatted information card
Calculate birth year from age
Determine if user is adult/minor

"""

# we will first ask for the user's details as name,age, email and city

name = input("Enter the name : ")
age = int(input("Enter the age : "))
email = input("Enter your email id :")
city = input("Enter the city name : ")

# look for @ symbol in email id address
if "@" in email:
    print("we do have a valid email id")
else:
    print("Please reenter the valid email id address including @")

adultOrMinor = "Adult"  # means its by default adult.
# validate the age
if 0 < age <= 120:
    print("You have mentioned the age " + str(age))
    # determin user is adult or minor by checking the age < 18
    if age < 18:
        adultOrMinor = "Minor"
    else:
        adultOrMinor = "Adult"

else:
    print("Please enter the valid age value (between 0-120)")

print(
    f"Hello {name}, your email id is {email}, of age {age} born in the year {2025 - age}, living in {city} is {adultOrMinor} "
)
