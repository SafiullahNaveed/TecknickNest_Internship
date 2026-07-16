# Wednesday Tasks

# Task-1 
# Write a program that compares two numbers and displays the larger number. 

# First we will take input from the user for two numbers

print("========================================")
print("Please Enter First Number: ")
num1 = int(input())
print("Please Enter Second Number: ")
num2 = int(input())
print("========================================")

# Checking to see which number is greater

if num1 > num2:
    print("========================================")
    print("The Larger Number is: ", num1)
else:
    print("========================================")
    print("The Larger Number is: ", num2)
    

# Adding empty print function to add some space between the tasks
print()


# Task-2 
# Write a program that classifies weather as Hot, Moderate, or Cold based on temperature entered by the user. 

# Asking the user for the temperature

print("========================================")
print("Please Enter the Temperature: ")
temp = int(input())
print("========================================")

# Checking the temperature and displaying the result

if temp > 30:
    print("==============================")
    print("The Weather is Very Hot !!")
elif temp >= 15:
    print("==============================")
    print("The Weather is Moderate")
else:
    print("==============================")
    print("The Weather is Cold")
    
# Bonus: Checking if the temperature is below freezing point or above boiling point

if temp < 0:
    print("================================")
    print("Please wear warm clothes!!")
if temp > 50:
    print("================================")
    print("It is Boiling Outside !!")
    

# Adding empty print function to add some space between the tasks
print()


# Task-3 
# Write a program that assigns grades (A, B, C, D, F) according to marks entered by the user. 

# Asking the user for the marks

print("===============================")
print("Please Enter Your Marks: ")
marks = int(input())
print("===============================")

if marks <= 0 or marks > 100:
    print("=============================")
    print("Please Enter Valid Marks !!")    
elif marks >= 90:
    print("==================")
    print("Your Grade is: A")
elif marks >= 80:
    print("==================")
    print("Your Grade is: B")
elif marks >= 70:
    print("==================")
    print("Your Grade is: C")
elif marks >= 60:
    print("==================")
    print("Your Grade is: D")
else:
    print("==================")
    print("Your Grade is: F")


# Adding empty print function to add some space between the tasks
print()

# Task-4 
# Write a program that determines whether a number is even or odd. 

# Asking the user for a number

print("===============================")
print("Please Enter a Number: ")
num = int(input())
print("===============================")

# Checking if the number is even or odd
if num % 2 == 0:
    print("==================")
    print("The Number is Even")
else:
    print("==================")
    print("The Number is Odd")


# Adding empty print function to add some space between the tasks
print()

# Task-5 
# Write a program that determines the ticket category (Child, Student, Adult) based on age. 

# Asking the user for their age
print("===============================")
print("Please Enter Your Age: ")
age = int(input())
print("===============================")

# Now we determine the ticket type based on the age entered by the user
if age < 12:
    print("===============================")
    print("Your Ticket Category is: Child")
elif age < 18:
    print("=================================")
    print("Your Ticket Category is: Student")
else:
    print("================================")
    print("Your Ticket Category is: Adult")