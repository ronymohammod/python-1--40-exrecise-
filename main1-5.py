# 1. Print numbers from 1 to 20 using while loop
print("-----------------------------------Print numbers from 1 to 20 using while loop--------------------------")
number = 1
while number <= 20:
    print(number)
    number += 1


print("-----------------------------------Print numbers txt from  using while loop--------------------------")
number = 1
while number <= 20:
    print(number, end=" ")
    number += 1
    numbers  ={"0"}
    print(" numbers ")


print("one line  from 2 add  using while loop ----")
number = 2
while number <= 20:
    print(number)
    number += 2








# 2. Print numbers from 1 to 20 using for loop
print("-------------------Print numbers from 1 to 20 using ____________for___________ loop-------------------")


# basic
print("basic for using")
for number in range(0, 23):
    print(number)




# All numbers on one line
print("all numbers in one line")
for number in range(1, 29):
    print(number, end=" ")


# Even numbers only
print("Even numbers only")
for number in range(2, 21, 2):
    print(number)






    # Odd numbers only
print(" Odd numbers only")
for number in range(1, 21, 2):
    print(number)






# Reverse order
print(" Revers order")
print(" Reverse order ")
for number in range(20, 0, -1):
    print(number)






#With custom text
print("------------------ print with custom text")
for number in range(11, 21):
    print(f"Current number is {number}")




#With squares
print("-----------------------for loop  with squares and cube ")
for number in range(1, 9):
    print(f"{number} squared = {number**3}")


    print(f"{number} cube = {number**3}")






    #Store in a list
print("-----------------------------------Store in a list------------")
numbers = [number for number in range(1, 21)]
print(numbers)






#Skip numbers (step size)
print("-------------------------Skip numbers (step size)--------------------------")
print("skip numbers (step size")
for number in range(1, 23, + 3):
    print(number)


for number in range(- 1, - 22, -3):
    print(number)




# Multiplication table (nested loop)
print("--------------Multiplication table ( nested loop)------")
for number in range(0, 11):
    print(f"Table of {number}:")




print("----------------Multiplier number------------------")
for multiplier in range(0, 6):
    print(f"{number} x {multiplier} = {number * multiplier}")
    print("-" * 20)




## 3. Print all even numbers between 1 to 50
print("-----------------------------print all even numbers between 1 to 50 ----------------")


#Triangle pattern of even numbers
print("Triangle pattern of even numbers")
for i in range(2, 31, 2):
    for j in range(2, i+1, 2):
        print(j, end=" ")
    print()










print("-----------Triangle pattern of even subtraction (-) numbers")


for i in range(1, 22,2):
    for j in range(1, i-2, 3):
        print(j, end=" ")
    print()




print("-------------------Triangle pattern of even Asterisk [Multication] (*) numbers" )


for i in range(1, 9,2):
    for j in range(1, i*5,  3):
        print(j, end=" ")
    print("-" * 2)




    print("-------------------Triangle pattern of  even Forward Slash] Divition (/) numbers" )


for i in range(1, 9,2):
    for j in range(1, i+5,  3):
        print(j, end=" / ")
    print()
   




#Pyramid pattern
print("-------------------- pattern of even Pyramid pattern_________")
for i in range(2, 51, 2):
    spaces = " " * (50 - i)
    numbers = " ".join(str(j) for j in range(2, i+1, 2))
    print(spaces + numbers)
print()




#Reverse triangle
print("---------------Reverse triangle---------------")
for i in range(50, 1, -2):
    for j in range(2, i+1, 2):
        print(j, end=" ")
print()




#Checkerboard style (rows of even numbers)
print("------------------Checkerboard style (rows of even numbers)---------")
for row in range(1, 6):
    for col in range(2, 51, 2):
        print(col, end=" ")
print()




#Even number multiplication table
print("--------------------Even number multiplication table-----------")
for number in range(2, 23, 2):
    print(f"Table of {number}:")
    for multiplier in range(1, 6):
        print(f"{number} x {multiplier} = {number * multiplier}")
print("-" * 20)






## 4. Print all odd numbers between 1 to 50
print("---------------------4 -___Print all odd numbers between-------------")




#Odd numbers only
("--------------------5 Odd numbers only-------------")
for number in range(1, 13, 2):
    print(number)


#Using condition inside loop
print("--------------------------Using condition inside loop----------")
for number in range(1, 11):
    if number % 2 != 0:
        print(number)


#Store odd numbers in a list
# print("----------------------------Store odd numbers in a list---------------")
odd_numbers = [number for number in range(1, 15) if number % 2 != 0]
print(odd_numbers)










#Multiplication table for odd numbers
print("--------------------------------Multiplication table for odd numbers-----------")
for number in range(1, 21, 2):
    print(f"Table of {number}:")
    for multiplier in range(1, 6):
        print(f"{number} x {multiplier} = {number * multiplier}")
    print("-" * 20)


    ## # Print numbers from 30 to 1 in reverse order
print("----------6 Print numbers from 30 to 1 in reverse order--------------")


for i in range(30, 0, -1):
    print(i)