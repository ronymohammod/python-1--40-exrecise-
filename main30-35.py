##31. Print this pattern:
# *
# **
# *
# **
# ***
print("# 31. Print this pattern *********")
# Print the pattern:
# *
# **
# *
# **
# ***


# Using print statements directly
print("*")
print("**")
print("*")
print("**")
print("***")




print("*")
print("**")
print("***")
print("****")
print("******")
print("**********")
print("*************")




# Alternative: Using a loop
print("---------# Alternative: Using a loop-------------")
pattern = ["*", "**", "*", "**", "***"]


for line in pattern:
    print(line)






# Print the pattern:
# 1
# 12
# 123
# 1234
# 12345
print(" Print the pattern:1, 12, 123, 1234, 12345 ,Using nested loops ")
 #Using nested loops
for i in range(1, 6):          # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for numbers in each row
        print(j, end="")       # Print numbers on the same line
    print()                    # Move to the next line




# 34. Print this pattern:
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1


print("--------------# 34. Print this pattern:5 5 5 5 5,4 4 4 4,3 3 3,2 2,1")
# Print the pattern:
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1


# Using nested loops
for i in range(5, 0, -1):          # Outer loop goes from 5 down to 1
    for j in range(i):             # Inner loop prints the number 'i' multiple times
        print(i, end=" ")          # Print the number with a space
    print()                        # Move to the next line


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


