# Wednesday Tasks

# Task-01
# Writing a program to print the pattern: 

print("===================================")
print("Task-01: Safiullah Naveed")
print("===================================")
for i in range(1, 6):
    print("* " * i) 
print("===================================")

# Task-02
# Writing a function table(number) that displays the multiplication table of a number. 

print("=============================================================")
print("Task-02: Safiullah Naveed")
print("=============================================================")
print("Please Enter the number to print its multiplication table:")
number = int(input())
def table(number):
    print("=======================================")
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)
    print("=======================================")

table(number)


# Task-03
# Writing a program to print a 5 × 5 star square pattern. 

print("===================================")
print("Task-03: Safiullah Naveed")
print("===================================")
for i in range(5):
    print("* " * 5)
print("===================================")

# Task-04
# Writing a function factorial(n) that calculates the factorial of a number. 

print("=====================================================")
print("Task-04: Safiullah Naveed")
print("=====================================================")
print("Please Enter a number to calculate its factorial:")
number = int(input())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("The factorial of", number, "is", factorial(number))
print("=====================================================")

# Task-05
# Writing a program that reverses a number.

print("=====================================================")
print("Task-05: Safiullah Naveed")
print("=====================================================")
print("Please Enter a number to reverse:")
number = int(input())
reversed_number = 0
while number > 0:
    reversed_number = reversed_number * 10 + number % 10
    number = number // 10
print("The reversed number is:", reversed_number)
print("=====================================================")