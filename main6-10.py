## 6. Print your name 10 times using loop
print("-------------------------Print your name 10 times using loop-----------")


# Print your name 10 times
for i in range(10):
    x = "What is Your Name?"
    print(x + " _Rony_")




## 6. Print your name is one line  15 times using loop
print("-------------------------------------------6 Print your name is one line  15 times using loop------------")


for i in range(15):
    print("My name ,", end=" ")










## 7. Print all numbers divisible by 3 from 1 to 100
print("----------------------------------------------------------7. Print all numbers divisible( % ) by 3 from 1 to 100-------------------------------------------------------------oooooooooo")
for i in range(1, 101):
    if i % 3 == 0:
        print(i, end=" ")




print("----------------------------------------------------------7. Print all numbers divisible( % ) by 3 from 1 to 100------one line-------------------------------------------------------oooooooooo")
for i in range(3, 101, 3):
    print(i)




## 8. Print all numbers divisible by 5 and 7 from 1 to 100
print("-------------------------------# 8. Print all numbers divisible by 5 and 7 from 1 to 100-----------------------")
# Print numbers divisible by both 5 and 7 from 1 to 100
for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i)


print("-------------------------------# 8. Print all numbers in ______one line__________ divisible by 5 and 7 from 1 to 100-----------------------")
for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end=" ")






## 9. Find the sum of numbers from 1 to 50
print("-----------------------# 9. Find the sum of numbers from 1 to 50--------------")
# Find the sum of numbers from 1 to 50
total = 0
for i in range(1, 51):
    total += i
print("The sum is:", total)




print("The sum is:", sum(range(1, 51)))




## 10. Find the sum of even numbers from 1 to 100
print("-----------------------# 10. Find the sum of even numbers from 1 to 100---------------------")
# Find the sum of even numbers from 1 to 100
total = 0
for i in range(2, 101, 2):  # start at 2, step by 2
    total += i
   
print("The sum of even numbers from 1 to 100 is:", total)


