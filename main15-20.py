# 16. Reverse a given number (e.g., 12345 → 54321)
print("------------------------# 16. Reverse a given number (e.g., 12345 → 54321)-----------------")
# Reverse a number using loop


num = int(input("Enter a number: "))
reverse_num = 0


while num > 0:
    digit = num % 10          # extract last digit
    reverse_num = reverse_num * 10 + digit
    num = num // 10           # remove last digit


print(f"Reversed number is {reverse_num}")




## 17. Find sum of digits of a number (e.g., 1234 = 1+2+3+4 = 10)
print("------------------# 17. Find sum of digits of a number (e.g., 1234 = 1+2+3+4 = 10)--------------")
# Sum of digits of a number


num = int(input("Enter a number: "))
sum_digits = 0


while num > 0:
    digit = num % 10         # extract last digit
    sum_digits += digit      # add digit to sum
    num = num // 10          # remove last digit


print(f"Sum of digits is {sum_digits}")








## 18. Count total number of digits in a number
print("----------------# 18. Count total number of digits in a number----------")
# Count total number of digits in a number


# Input number from user
num = int(input("Enter a number: "))


# Initialize counter
count = 0


# Loop until number becomes 0
while num != 0:
    num //= 10   # Remove last digit
    count += 1   # Increase digit count


# Print result
print("Total number of digits:", count)






# 19. Print square of numbers from 1 to 15
print("-----------squares of numbers from 1 to 15--------")
for i in range(1, 16):
    print(f"The square of {i} is {i*i}")




## 20. Print cube of numbers from 1 to 12
print("---------# 20. Print cube of numbers from 1 to 12--------")
# Print cubes of numbers from 1 to 12


for i in range(1, 13):
    print(f"The cube of {i} is {i**3}")
