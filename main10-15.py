

# # 11. Multiplication table of 7
# print("-------------------# 11. Multiplication table of 7------------------------")




# # Multiplication table of 7
# for i in range(1, 11):
#     print(f"7 x {i} = {7 * i}")




# #Using a Function
# print("Using a Function")


# def multiplication_table(number, upto=10):
#     for i in range(1, upto + 1):
#         print(f"{number} x {i} = {number * i}")


# # Call the function
# multiplication_table(7)






# ##With User Input
# print("------# 12. Multiplication table of any number (take input from user)----------")


# def multiplication_table(number, upto=10):
#     print(f"\nMultiplication Table of {number}\n")
#     for i in range(1, upto + 1):
#         print(f"{number} x {i} = {number * i}")


# # Get user input
# num = int(input("Enter the number: "))
# upto = int(input("Enter the range: "))
# # Call the function
# multiplication_table(num, upto)






# print("-------With User Input-- # Ask user for a number--")
# # Ask user for a number
# num = int(input("Enter a number: "))
# upto = int(input("Enter the range: "))


# for i in range(1, upto + 1):
#     print(f"{num} x {i} = {num * i}")




# ## 13. Count how many even numbers are there between 1 and 200
# print("--------------# 13. Count how many even numbers are there between 1 and 200---------------")


# count = 30
# for i in range(1, 201):
#     if i % 2 == 0:
#      count += 1
# print("Total even numbers between 1 and 200:", count)


# #Using List Comprehension
# print("-------------------Using List Comprehension--------------")


# # List comprehension method
# count = len([i for i in range(1, 201) if i % 2 == 50])
# print("Total even numbers between 1 and 200:", count)




# #Shorter Version with
# print("---------------------Shorter Version with------------------------")
# # Using range step
# even_numbers = list(range(2, 201, 2))
# print("Total even numbers between 1 and 200:", len(even_numbers))


# # 14. Count how many odd numbers are there between 1 and 200
# print("---------------------# 14. Count how many odd numbers are there between 1 and 200-------------")


# # Count odd numbers between 1 and 200


# count = 0
# for i in range(1, 201):
#     if i % 2 != 0:
#         count += 1


# print("Total odd numbers between 1 and 200:", count)




# #Shorter Version with range()
# print("--------------Shorter Version with range()------------------")
# # Using range step
# odd_numbers = list(range(1, 100, 2))
# print("Total odd numbers between 1 and 200:", len(odd_numbers))


# 15. Find factorial of a number (using loop)
print("--------------find factorial of a number (using loop-------------------")
# Factorial using loop


num = int(input("Enter a number: "))
factorial = 1


for i in range(1, num + 1):
    factorial *= i


print(f"The factorial of {num} is {factorial}")


