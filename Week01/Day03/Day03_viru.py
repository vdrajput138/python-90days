"""
1. Extract the first 3 characters and last 3 characters of a given string
"""

value_to_extract = input("Please provide the string value: ")
print(f"First 3 characters of the string are : {value_to_extract[:3]} and last 3 characters of the string are : {value_to_extract[-3:]}")


"""
2. Convert a string to uppercase, lowercase, and title case
"""
print("\nWe have a word as JUSTIFICATION")
sample_word = "JUSTIFICATION"
print(f"The lowercase is {sample_word.lower()}")
print(f"The Title is  {sample_word.title()}")
print("\nWe have word as Clarification")
sample_word = "Clarification"
print(f"The uppercase is {sample_word.upper()}")


"""
3. Write a program that reverses a given string
"""

to_be_reverse = input("Please enter the string to reverse: ")
print("Reverse string of the provided string is "+ to_be_reverse[::-1])


"""
4. Create a function that checks if a string is a palindrome (reads same forwards and backwards)
"""
def verifyPalindrome(word):
    return word == word[::-1]


to_be_verify_palindrome = input("Please enter the string value to verify about palindrome: ")
result = verifyPalindrome(to_be_verify_palindrome)

if result:
    print("Given input is a palindrome")
else:
    print("Given word is not palindrome")

"""
5. Write a program that removes all spaces from a string and replaces them with underscores
"""
given_string = input("Please mention the sentense or a multiple words: ")
print("updated version of the given string is : "+ given_string.replace(" ","_"))


"""
6. Build a function that takes a sentence and returns it with each word capitalized and words sorted alphabetically
"""
input_sentence = input("Please enter the sentense to sort alphabetically: \n\t")
final_sentence = input_sentence.split(" ")
# for i in final_sentence:
#     final_sentence[i] = final_sentence[i].title()
final_sentence = [word.title() for word in final_sentence]
final_sentence.sort()
print("The sorted sentense is :" + " ".join(final_sentence))