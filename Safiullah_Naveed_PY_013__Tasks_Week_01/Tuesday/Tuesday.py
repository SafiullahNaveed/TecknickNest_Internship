# Tuesday Taska
# Task-01

# We will write a program tocheck whether the person is eligible for voting or not
# We will simply take input from the user and check the age

print("==========================")
print("Please Enter Your Age !!")
print("==========================")
age = int(input())

# Then use if else statement to check the age and display the result

if age >= 100 or age < 0:
    print("Please Enter a Valid Age !!")
else:
    if age >= 18:
        print("===============================")
        print("You are eligible for voting !!")
        print("===============================")
    else:
        print("===================================")
        print("You are not eligible for voting !!")
        print("===================================")


# Adding empty print function to add some space between the tasks
print()
        
# Task-02
# We will write a program to check whether the student has passed or failed in the exam

# Asking for input from the user

print("================================")
print("Please Enter Your Marks !!")
print("================================")
marks = int(input())

# Checking the marks (Below 30 is fail and above 30 is pass)

if marks >= 100 or marks < 0:
    print("==============================")
    print("Please Enter Valid Marks !!")
    print("==============================")
else:
    if marks >= 30:
        print("==============================")
        print("You have passed the exam !!")
        print("==============================")
    else:
        print("==============================")
        print("You have failed the exam !!")
        print("==============================")
        
        
# Adding empty print function to add some space between the tasks
print()

# Task-03
# We will write a program to check if the username entered matches "admin" or not

# Asking for input from the user

print("Please Enter Your Username !!")
username = input()

# Checking the username entered by the user

if username == "admin":
    print("===================================")
    print("The Username entered is correct !!")
    print("===================================")
else:
    print("=====================================")
    print("The Username entered is incorrect !!")
    print("=====================================")
    
    
# Adding empty print function to add some space between the tasks
print()
    
# Task-04
# Writing a program that determines whether a student is eligible for a scholarship based on 

# Taking input from the user for name, cgpa, attendance and family income

print("===========================")
print("Please Enter Your Name: ")
print("===========================")
Name = input("Name: ")

print("============================")
print("Please Enter Your CGPA: ")
print("============================")
cgpa = float(input())

print("================================")
print("Please Enter Your Attendance: ")
print("================================")
attendance = int(input())

print("==================================")
print("Please Enter Your Family Income: ")
print("==================================")
income = int(input())

# Calculating the scholarship eligibility based on the given criteria

if cgpa>= 3.5 and attendance >= 80:
    if income < 100000:
        print("==================")
        print("Full Scholarship")
    else:
        print("==================")
        print("Merit Scholarship")

elif cgpa >= 3:
    print("======================")
    print("Partial Scholarship")
else:
    print("========================")
    print("Sorry!! No Scholarhip")


# Adding empty print function to add some space between the tasks
print()

# Task-
# Writng a program to check whether the number is positive, negative or zero

# First taking input from the user

print("=========================")
print("Please Enter a Number: ")
print("=========================")
number = int(input())

# Checking the number entered by the user and displaying the result

if number > 0:
    print("===========================")
    print("The Number is Positive !!")
elif number < 0:
    print("===========================")
    print("The Number is Negative !!")
else:
    print("=======================")
    print("The Number is Zero !!")
