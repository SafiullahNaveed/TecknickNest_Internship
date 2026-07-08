# Task-1 
# Write a program that calculates a student's total marks, average marks, and pass/fail status. 

# Asking the user for the marks of three subjects
print("========================================")
print("Please Enter Marks for Subject 1: ")
sub1 = float(input())
print("Please Enter Marks for Subject 2: ")
sub2 = float(input())
print("Please Enter Marks for Subject 3: ")
sub3 = float(input())
print("========================================")

# Calculating total marks and average marks
total_marks = sub1 + sub2 + sub3
average_marks = total_marks / 3

# Checking pass/fail status (Passing Marks are 30)
if average_marks >= 30:
    print("=========================")
    print("Student has passed.")
else:
    print("=========================")
    print("Student has failed.")

# Displaying the results
print("========================================")
print("Total Marks: ", total_marks)
print("Average Marks: ", average_marks)
print("========================================")

# Adding empty print function to add some space between the tasks
print()

# Task-2 
# Write a program that checks whether a student is eligible for university admission based on age and intermediate percentage. 

# Asking the user for age and intermediate percentage

print("============================================")
print("Please Enter Your Age: ")
age = int(input())
print("Please Enter Your Intermediate Percentage: ")
percentage = float(input())
print("============================================")

# Checking eligibility for university admission (Age should be >= 17 and Percentage should be >= 50)
if age >= 17 and percentage >= 50:
    print("============================================")
    print("You are eligible for university admission.")
else:
    print("============================================")
    print("You are not eligible for university admission.")
    

# Adding empty print function to add some space between the tasks
print()

# Task-3 
# Write a program that determines whether an employee qualifies for a bonus based on salary and years of experience.

 
# Asking the user for salary and years of experience

print("============================================")
print("Please Enter Your Salary: ")
salary = float(input())
print("Please Enter Your Years of Experience: ")
experience = int(input())
print("============================================")

# Now we check if the employee qualifies for the bonus
# The salary should be >= 50000 and experience should be >= 5 years to qualify for the bonus

if salary >= 50000 and experience >= 5:
    print("==============================================")
    print("Congratulations!! You qualify for the bonus.")
else:
    print("============================================")
    print("Sorry !! You do not qualify for the bonus.")
    
# Adding empty print function to add some space between the tasks
print()

# Task-4 
# Write a program that checks whether a bank account has sufficient balance for a withdrawal request.

# Asking the user for current balance and withdrawal amount

print("============================================")
print("Please Enter Your Current Balance: ") 
current_balance = float(input())

print("Please Enter Your Withdrawal Amount: ")
withdrawal_amount = float(input())
print("============================================")

# Now we check if the account has sufficient balance for the withdrawal request
if current_balance >= withdrawal_amount:
    print("================================")
    print("Withdrawal Successful !!")
else:
    print("============================================")
    print("Withdrawal Failed !! Insufficient Balance.")
    
# Adding empty print function to add some space between the tasks
print()

# Task-5 
# Write a program that determines scholarship status (Full Scholarship, Partial Scholarship, or Not Eligible) using CGPA, attendance, and family income.

print("============================================")
print("Please Enter Your CGPA: ")
cgpa = float(input())
print("Please Enter Your Attendance Percentage: ")
attendance = float(input())
print("Please Enter Your Family Income: ")
family_income = float(input())
print("============================================")

# Determining scholarship status
if cgpa >= 3.5 and attendance >= 80 and family_income <= 500000:
    print("============================================")
    print("You are eligible for Full Scholarship.")
elif cgpa >= 3.0 and attendance >= 70 and family_income <= 1000000:
    print("============================================")
    print("You are eligible for Partial Scholarship.")
else:
    print("============================================")
    print("You are not eligible for any scholarship.")