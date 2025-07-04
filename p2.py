# Question 1
number = float(input("Enter a number: "))
if number > 0:
  print("Positive")
elif number < 0:
  print("Negative")
else:
  print("Zero")

# Question 2
number = int(input("Enter an integer: "))
if number % 2 == 0:
  print("Even")
else:
  print("Odd")

# Question 3
age = int(input("Enter your age: "))
if age >= 18:
  print("Eligible to vote")
else:
  print("Not eligible")

# Question 4
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
  print("Divisible by both 3 and 5")
elif number % 3 == 0:
  print("Divisible by 3")
elif number % 5 == 0:
  print("Divisible by 5")
else:
  print("Not divisible by 3 or 5")

# Question 5
marks = float(input("Enter student's marks: "))
if marks >= 90:
  print("A+")
elif marks >= 80:
  print("A")
elif marks >= 70:
  print("B")
else:
  print("Fail")

# Question 6
temperature = float(input("Enter the temperature: "))
if temperature > 40:
  print("Too hot")
elif temperature < 10:
  print("Too cold")
else:
  print("Moderate weather")

# Question 7
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print("Leap year")
else:
  print("Not a leap year")

# Question 8
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest = num1
if num2 > largest:
  largest = num2
if num3 > largest:
  largest = num3

print("The largest number is:", largest)

# Question 9
password = input("Enter the password: ")
if password == "admin123":
  print("Access granted")
else:
  print("Access denied")

# Question 10
number = int(input("Enter an integer: "))
if number > 0:
  print("Number is positive")
  if number < 100:
    print("Number is less than 100")
  else:
    print("Number is not less than 100")
else:
  print("Number is not positive")