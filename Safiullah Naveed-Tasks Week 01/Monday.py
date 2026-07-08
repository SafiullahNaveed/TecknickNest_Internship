# Monday Tasks
# Task-01

# Using simple print statements to display all the required information
print("Name: Safiullah Naveed")
print("Department: AI")
print("Semester No.: 02")
print("My Favourite Programming language is Python") # Because it is easy to understand but powerfull and used heavily in my field (AI)

# Adding empty print function to add some space between the tasks
print()


# Task-02
# Take input from the user and Display it neatly

print("Please Enter Your Name !!")
name = input("Name: ")
print("Please Enter Your Age !!")
age = input("Age: ")

# Input was taken separately now displaying it neatly
print("=========================")
print("Name: ", name)
print("Age: ", age)
print("==========================")

# Adding empty print function to add some space between the tasks
print()

# Task-03
# Take input from user and calculate the area

print("Please Enter the Length !!")
length = float(input("Length: "))
print("Please Enter the Width")
width = float(input("Width: "))

# After taking input using simple formula to calculate the area
area = length * width

print("==========================")
print("The Area is: ", area , "sq")
print("==========================")


# Adding empty print function to add some space between the tasks
print()

# Task-04
# Take input from user and calculate the total marks

# Taking input for all the marks
print("Please Enter Marks for Programming !!")
prog_mrks = float(input("Marks: "))
print("Please Enter Marks for Maths Subject !!")
math_mrks = float(input("Marks: "))
print("Please Enter Marks for English Subject !!")
eng_mrks = float(input("Marks: "))

# Now calculating total marks

total_mrks = prog_mrks + math_mrks + eng_mrks
avg_mrks = total_mrks / 3

# Now displaying all the Results

print("=========================================")
print("Prgramming Marks: ", prog_mrks)
print("Maths Marks: ", math_mrks)
print("English Marks: ", eng_mrks)

print("Total Marks: ", total_mrks)
print("Average Marks: ", avg_mrks)

print("==========================================")


# Adding empty print function to add some space between the tasks
print()


# Task-05
# Take input from user and calculating the total Expenses

# Taking input for all the Expenses
print("Please Enter Expenses for Food !!")
food = float(input("Food Expenses: "))
print("Please Enter Expenses for Transport !!")
transport = float(input("Transport Expenses: "))
print("Please Enter Expenses for Internet !!")
internet = float(input("Internet Expenses: "))

# Now calculating the Total Expenses

total_Expenses = food + transport + internet

# Now displaying all the Results

print("=========================================")
print("Food Expenses: ", food, "PKR")
print("Transport Expenses: ", transport, "PKR")
print("Internet Expenses: ", internet, "PKR")

print("Total Expenses: ", total_Expenses, "PKR")

print("==========================================")