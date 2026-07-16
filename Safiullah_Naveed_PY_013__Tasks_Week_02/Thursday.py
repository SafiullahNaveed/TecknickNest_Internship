# Thursday Taks

# Task-01
# Writing a function that returns grades A, B, C, D, or F. 

def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
    
print ("==========================================================")
print("Task-01: Safiullah Naveed")
print ("==========================================================")
score = int(input("Please enter your Marks: "))
if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
else:
    print("The grade for the score", score, "is:", grade(score))
print ("==========================================================")

# Task-02
# Writing a program to print the following pattern: 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

print ("==========================================================")
print("Task-02: Safiullah Naveed")
print ("==========================================================")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print ("==========================================================")

# Task-03
# Writing a function that returns the total marks of three subjects. 

print ("==========================================================")
print("Task-03: Safiullah Naveed")
print ("==========================================================")
def calculate_total(a, b, c):
    return a + b + c

print("Please Enter the marks of three subjects:")
sub1 = int(input("Please Enter marks of subject 1: "))
sub2 = int(input("Please Enter marks of subject 2: "))
sub3 = int(input("Please Enter marks of subject 3: "))

total = calculate_total(sub1, sub2, sub3)
print("The total marks are:", total)
print ("==========================================================")

# Task-04
# Writing a function that returns the average marks. 

print ("==========================================================")
print("Task-04: Safiullah Naveed")
print ("==========================================================")
def calculate_average(total):
    return total / 3

print("Please Enter the marks of three subjects:")
sub1 = int(input("Please Enter marks of subject 1: "))
sub2 = int(input("Please Enter marks of subject 2: "))
sub3 = int(input("Please Enter marks of subject 3: "))
total = calculate_total(sub1, sub2, sub3)

print("The average marks are:", calculate_average(total))
print ("==========================================================")

# Task-05
# Create a Student Result Management System.

print ("==========================================================")
print("Task-05: Safiullah Naveed")
print ("==========================================================")

# I will create a Result Management System that will taka the marks of three subjects and will calcuate the total marks, the grade and the average mnarks.

def calculate_total(a, b, c):
    return a + b + c

def calculate_average(total):
    return total / 3

print("Please Enter the marks of three subjects:")
sub1 = int(input("Please Enter marks of subject 1: "))
sub2 = int(input("Please Enter marks of subject 2: "))
sub3 = int(input("Please Enter marks of subject 3: "))

total = calculate_total(sub1, sub2, sub3)
grade = grade(total)

average = calculate_average(total)

print("The total marks are:", total)
print("The grade is:", grade)
print("The average marks are:", calculate_average(total))
print ("==========================================================")