# Monday Tasks
# Task-01 

# We will be print numbers from 1 to 10 using a for loop.

print("==================================")
print("Task-01: Safiullah Naveed")
print("==================================")
for i in range(1, 11):
    print(i)


# Now we add an empty line to separate the tasks.
print()


# Task-02
# We will write a function greet() and call it three times.

print("==================================")
print("Task-02: Safiullah Naveed")
def greet():
    print("Welcome to Python Programming !!!")

print("==================================")
greet()
greet()
greet()
print("==================================")

# Add an empty line to separate the tasks.
print()

# Task-03
# Writing a program to print all even numbers from 2 to 20.

print("==================================")
print("Task-03: Safiullah Naveed")
print("==================================")
for i in range(2, 21, 2):
    print(i)

print("==================================")


# Adding an empty line to separate the tasks.
print() 

# Task-04
# Writing a function to return the square of a number.

print("==================================")
print("Task-04: Safiullah Naveed")
print("==================================")

def square(num):
    return num * num

print(square(5))
print("==================================")

# Adding an empty line to separate the tasks.
print() 


# Task-05
# Writing a program to calculate the sum of numbers of 1 to n

print("===========================================")
print("Task-05: Safiullah Naveed")  
print("===========================================")

print("Please Enter a Number: ")
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
print("The sum of numbers from 1 to", n, "is:", sum)
print("=========================================== ")
