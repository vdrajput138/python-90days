"""

## 📚 Topics Covered
- Functions - Basics
- Parameters and Arguments
- Return Values


## 💻 Practice Questions

Complete these exercises to reinforce your learning:

1. Write a function to check if a number is prime.

2. Create a function that returns the factorial of a number using recursion.

3. Write a function to calculate the area of a circle given its radius.

4. Create a function that takes a list and returns the sum of all even numbers.

5. Write a function to convert Celsius to Fahrenheit and vice versa.

6. Create a function that accepts variable number of arguments (*args) and returns their average.

7. Write a function to check if a string is a palindrome (ignore case and spaces).

8. Create a function that returns both quotient and remainder of two numbers as a tuple.

9. Write a function to find the maximum of three numbers without using max().

10. Create a function that validates if an email format is correct (basic check for @ and .).


"""

"""
1. Write a function to check if a number is prime.

"""

from math import sqrt


def check_number_prime(num):
    result = True

    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            result = False
            print(f"The number {num} is not prime")
            break
    if result:
        print(f"The number {num} is prime")
    return result


# resultPrime = check_number_prime(87)
# resultPrime = check_number_prime(89)
# resultPrime = check_number_prime(93)
# resultPrime = check_number_prime(97)
# resultPrime = check_number_prime(71)
# resultPrime = check_number_prime(67)
# resultPrime = check_number_prime(53)
# resultPrime = check_number_prime(43)
# if resultPrime:
#     print("The number is prime")
# else:
#     print("The number is not prime")

"""

2. Create a function that returns the factorial of a number using recursion.

"""


def multiplyNum(num):
    result = 1
    if num > 1:
        result = multiplyNum(num - 1)
    result *= num
    return result


mnum = multiplyNum(5)
print(f"Result is {mnum}")
