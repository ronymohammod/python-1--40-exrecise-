

# 35. Create a list of 10 numbers and print sum and average of all numbers
print("-----------------# 35. Create a list of 10 numbers and print sum and average of all numbers-----------")




# Input: 10 numbers from the user
numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)


# Calculate sum
total = 0
for num in numbers:
    total += num


# Calculate average
average = total / len(numbers)


# Print results
print("Numbers entered:", numbers)
print("Sum of numbers:", total)
print("Average of numbers:", average)




# 36. Count how many numbers are greater than 50 in a list
print("--------------------------------# 36. Count how many numbers are greater than 50 in a list--------")
# Count how many numbers are greater than 50 in a list


# Input: 10 numbers from the user
numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)


# Count numbers greater than 50
count = 0
for num in numbers:
    if num > 50:
        count += 1


# Print results
print("Numbers entered:", numbers)
print("Count of numbers greater than 50:", count)




# 37. Take 5 student names and their marks, then print average marks
print("-----------# 37. Take 5 student names and their marks, then print average marks---------")
# Take 5 student names and their marks, then print average marks


students = []
marks = []


# Input: 5 student names and marks
for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    mark = float(input(f"Enter marks of {name}: "))
    students.append(name)
    marks.append(mark)


# Calculate average marks
total = 0
for m in marks:
    total += m


average = total / len(marks)


# Print results
print("\nStudent Marks:")
for i in range(5):
    print(f"{students[i]}: {marks[i]}")


print("\nAverage Marks:", average)






# 38. Create a dictionary of 5 students (name: marks) and print all names and marks
print("----# 38. Create a dictionary of 5 students (name: marks) and print all names and marks-------")
# Create a dictionary of 5 students (name: marks) and print all names and marks


# Input: 5 student names and marks
students = {}


for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    mark = float(input(f"Enter marks of {name}: "))
    students[name] = mark


# Print all names and marks
print("\nStudent Marks:")
for name, mark in students.items():
    print(f"{name}: {mark}")




# 39. Take a sentence and count how many words are there
print("-----------# 39. Take a sentence and count how many words are there---------")
# Take a sentence and count how many words are there


# Input sentence from user
sentence = input("Enter a sentence: ")


# Split sentence into words
words = sentence.split()


# Count words
count = len(words)


# Print results
print("Sentence entered:", sentence)
print("Number of words:", count)




# 40. Take a list of numbers and create two new lists: one for even numbers and one for odd numbers
print("------------# 40. Take a list of numbers and create two new lists: one for even numbers and one for odd numbers--------")
# Take a list of numbers and create two new lists: one for even numbers and one for odd numbers


# Input: numbers from the user
numbers = []
n = int(input("How many numbers do you want to enter? "))


for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)


# Separate even and odd numbers
even_numbers = []
odd_numbers = []


for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)


# Print results
print("\nNumbers entered:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)




#     start += 1









