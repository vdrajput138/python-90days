"""
1. Create three variables: one int, one float, one string; print each and their types.

"""
int_val = 30
float_val = 30.30
string_val = "30.30.30"
print("Type for "+ str(int_val)+ " is -" + str(type(int_val).__name__))
print("Type for "+ str(float_val)+ " is - "+ str(type(float_val).__name__))
print("Type for "+ string_val + " is - " + str(type(string_val).__name__))


"""
2. Perform arithmetic with int/float (add, subtract, multiply, divide); print results.

"""
print("Int values calculation")
print("First value is 10")
print("Second value is 2")
a = 10
b = 2
print(f"a+b = {a+b}")
print(f"a-b = {a-b}")
print(f"a*b = {a*b}")
print(f"a/b = {a/b}")
print("Float Values calculation")
print("First value is 121.0")
print("Second value is 11.0")
a = 121.0
b = 11.0
print(f"a+b = {a+b}")
print(f"a-b = {a-b}")
print(f"a*b = {a*b}")
print(f"a/b = {a/b}")

"""
3. Create a boolean variable, test its truth value in an if statement and print a message.

"""
check_val = True
if check_val:
    print("This is the true condition")
else:
    print("This is the false condition")

"""
4. Write a script that takes two numeric inputs from the user, performs all arithmetic operators (+,-,,/,//, %,*), and prints formatted results.

"""
x,y = input("Please enter 2 numeric value: ").split()
x = int(x)
y = int(y)
print("Arithmatic operation for your provided inputs are as follows: ")
print(f"The addition is : {x+y}")
print(f"The substraction is : {x -y}")
print(f"The multiplication is : {x * y}")
print(f"The division is : {x/y}")

"""
5. Ask user for their birth year, current year; compute their age; then compute how many seconds they've lived approximately.

"""
birth_year = int(input("Please enter the birth year: "))
current_year = int(input("Please enter the current year: "))
total_years = current_year - birth_year
print("Total seconds you have lived till this years - "+ str(total_years * 365 * 24 * 60 * 60))


"""
6. Write a small “unit converter” script: user inputs value + unit (e.g., “10 km”), and converts it to a different unit (e.g., miles) using appropriate logic and formatting.
"""

print("This is about converting Kilometers to meters")
km_value = int(input("Please enter value for Kilometers - "))
print("The converted value of kilometers into meters is - "+ str(km_value * 1000))