# Tuesday Tasks

# Task-01
# Writing a program that prints numbers from 1 to 10 using a while loop. 

print("===================================")
print("Task-01: Safiullah Naveed")
while True:
    print("===================================")
    for i in range(1, 11):
        print(i)
    break
print("===================================")

# Task-02
# Writing a function largest(a, b) that returns the larger number. 

print("===================================================")
print("Task-02: Safiullah Naveed")
def largest(a, b):
    if a > b:
        return a
    else:
        return b

print("===================================================")
print("Please Enter two numbers to find the largest one:")  
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The largest number is:", largest(a, b))
print("===================================================")

# Task-03
# Writing a program that prints the multiplication table of a number entered by the user. 

print("================================================================")
print("Task-03: Safiullah Naveed")
print("================================================================")
num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
print("================================================================")

# Task-04
# Writing a function that determines whether a number is even or odd. 

print("===============================================================")
print("Task-04: Safiullah Naveed")
def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print("===============================================================")
def check_even(number):
    return number % 2 == 0

num = int(input("Enter a number to check if it's even or odd: "))

if check_even(num):
    print("The number is even.")
else:
    print("The number is an odd number.")

print("================================================================")



# Task-05
# Writing a program that counts how many digits are present in a number.

# First we will take input from the user and then we will use a while loop to count the number of digits in the number.
    
print("===============================================================")
print("Task-05: Safiullah Naveed")
num = int(input("Please enter a number: "))
count = 0
temp = num
if temp == 0:
    count = 1
while temp > 0:
    count += 1
    temp //= 10
print("The number of digits in", num, "is:", count)
print("================================================================")