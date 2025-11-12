"""
User Profile Generator: Practice String Operations & data types.
Flow:
    # Step 1: Collect user information
    # Step 2: Process strings and numbers
    # Step 3: Generate formatted profile

"""

print("User Profile Generator")
print("=" * 40)

# Collect user data
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height(in meter): "))
favorite_color = input("Enter your Favorite Color: ")
is_student = input("Are you a student (Y/N): ").lower() in (
    "y",
    "yes",
    "Y",
    "N",
    "No",
    "Yes",
    "no",
)

# String Operations
username = name.lower().replace(" ", "_") + str(age)
name_upper = name.upper()
name_length = len(name)
initials = "".join([word[0].upper() for word in name.split()])

# Boolean logic
status = "Student" if is_student else "Professional"

# Display profile
print(f"\n🎉 Profile Created Successfully!")
print(f"📛 Name: {name} (Length: {name_length} characters)")
print(f"🔠 Uppercase: {name_upper}")
print(f"🆔 Username: {username}")
print(f"🎯 Initials: {initials}")
print(f"🎂 Age: {age} (Type: {type(age)})")
print(f"📏 Height: {height}m (Type: {type(height)})")
print(f"🎨 Favorite Color: {favorite_color}")
if status in ("N", "No", "no"):
    print(f"📚 Status: {status} (Type: {type(is_student)})")
else:
    print(f"😎 Status: {status} (Type: {type(is_student)})")
