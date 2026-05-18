## 21. Check whether a number is positive, negative or zero
print("-------------------------# 21. Check whether a number is positive, negative or zero-----------------")
# Check whether a number is positive, negative or zero


num = int(input("Enter a number: "))


if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")






## 22. Check if a number is even or odd
print("---------------## 22. Check if a number is even or odd-----------")
# Check if a number is even or odd


num = int(input("Enter a number: "))


if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")






# 23. Find the largest number among three numbers
print("=------------------------# 23. Find the largest number among three numbers------------")
# Find the largest number among three numbers


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))


if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")


##24. Check if a year is leap year or not
print("__________-# 24. Check if a year is leap year or not-----_____________")
# Check if a year is leap year or not


year = int(input("Enter a year: "))


if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not a Leap Year")




##25. Print all vowels from a given string
print("-----------------# 25. Print all vowels from a given string--------")
# Print all vowels from a given string


text = input("Enter a string: ")
vowels = "aeiouAEIOU"


print("Vowels in the string are:")
for char in text:
    if char in vowels:
        print(char, end=" ")


