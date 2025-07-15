# Assignment #12 – Modules, Functions & Built-ins

# 1️⃣ math module & double()
import math

def double(n):
    return n * 2

print("Factorial of 5:", math.factorial(5))
print("Double of 6:", double(6))

# 2️⃣ random module, greet(), len()
import random

names = ["Ali", "Sara", "Ahmed", "Zara"]
def greet(name):
    print("Hello,", name + "!")

random_name = random.choice(names)
greet(random_name)
print("Length of names list:", len(names))

# 3️⃣ sum(), statistics, is_even()
import statistics

marks = [45, 65, 75, 80]
def is_even(num):
    return num % 2 == 0

print("Sum of marks:", sum(marks))
print("Average:", statistics.mean(marks))
print("Is 45 even?", is_even(45))

# 4️⃣ datetime.now(), say_hello(), type()
import datetime

def say_hello():
    print("Hello there!")

now = datetime.datetime.now()
say_hello()
my_var = 3.14
print("Current time:", now)
print("Type of my_var:", type(my_var))

# 5️⃣ area_of_circle(), math.pi
def area_of_circle(radius):
    return math.pi * radius * radius

radius = 7
area = area_of_circle(radius)
print("Area of circle:", area)
print("Type of area:", type(area))

# 6️⃣ random.randint(), check_number()
def check_number(num):
    if num > 50:
        print(num, "is greater than 50")
    else:
        print(num, "is 50 or less")

rand_num = random.randint(10, 100)
print("Random number:", rand_num)
check_number(rand_num)

# 7️⃣ max(), math.pow(), display_info()
def display_info(name, age):
    print("Name:", name)
    print("Age:", age)

numbers = [4, 10, 15, 3]
print("Max value:", max(numbers))
print("2^3 using math.pow:", math.pow(2, 3))
display_info("Hashim", 20)

# 8️⃣ calendar.month(), len(), show_message()
import calendar

def show_message():
    print("Keep learning Python! 💻")

print(calendar.month(2025, 5))
msg = "Hello from AI Hub!"
print("Message length:", len(msg))
show_message()

# 9️⃣ os.getcwd(), str(), multiply()
import os

def multiply(x, y):
    return x * y

print("Current Directory:", os.getcwd())
num = 100
num_str = str(num)
print("String form:", num_str)
print("Product of 4 and 5:", multiply(4, 5))

# 🔟 sqrt(), user input, type(), print result
def calculate_square_root(num):
    return math.sqrt(num)

user_input = input("Enter a number: ")
num = int(user_input)
print("Type of input:", type(num))
print("Square root:", calculate_square_root(num))
