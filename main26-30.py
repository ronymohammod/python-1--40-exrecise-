# 26. Count vowels and consonants in a string
print("----------------# 26. Count vowels and consonants in a string------------")
# Count vowels and consonants in a string


text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0


for char in text:
    if char.isalpha():  # check if character is a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1


print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")










# 27. Print characters of a string one by one using loop
print("# 27. Print characters of a string one by one using loop-----------------")
# Print characters of a string one by one


text = input("Enter a string: ")


print("Characters in the string are:")
for char in text:
    print(char)










# 28. Reverse a string using loop (without using slicing)
print("--------------# 28. Reverse a string using loop (without using slicing)---------")




# Input string
text = input("Enter a string: ")


# Initialize an empty string to store the reversed result
reversed_text = ""


# Loop through the string in reverse order
for char in text:
    reversed_text = char + reversed_text


# Print the reversed string
print("Reversed string:", reversed_text)






# 29. Find the largest number from a list of 10 numbers
print("--------------------------# 29. Find the largest number from a list of 10 numbers-----------")


# Input: 10 numbers from the user
numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)


# Initialize largest with the first number
largest = numbers[0]


# Loop through the list to find the largest
for num in numbers:
    if num > largest:
        largest = num


# Print the largest number
print("The largest number is:", largest)






# 30. Find the smallest number from a list of 10 numbers
print("---------------# 30. Find the smallest number from a list of 10 numbers-------------")




# Input: 10 numbers from the user
numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)


# Initialize smallest with the first number
smallest = numbers[0]


# Loop through the list to find the smallest
for num in numbers:
    if num < smallest:
        smallest = num


# Print the smallest number
print("The smallest number is:", smallest)




