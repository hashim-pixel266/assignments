ull_name = input("Enter your full name: ")
print("Number of characters in name:", len(full_name))

# 2️⃣ Create a list of 5 names and print names with more than 5 characters
names = ["Ali", "Moazzam", "Fatima", "Zara", "Hashim"]
long_names = [name for name in names if len(name) > 5]
print("Names with more than 5 characters:", long_names)

# 3️⃣ Ask for a sentence, convert to lowercase, and check for "python"
sentence = input("Enter a sentence: ")
if "python" in sentence.lower():
    print("The word 'python' is present.")
else:
    print("The word 'python' is not present.")

# 4️⃣ Create list of numbers and print numbers divisible by 3
numbers = [4, 9, 12, 15, 22, 18, 7]
div_by_3 = [num for num in numbers if num % 3 == 0]
print("Numbers divisible by 3:", div_by_3)

# 5️⃣ Input number and check if it's positive, negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 6️⃣ Take two input numbers and print the greater one
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("Greater number is:", num1)
else:
    print("Greater number is:", num2)

# 7️⃣ Create list of cities and add a new one
cities = ["Lahore", "Karachi", "Islamabad", "Multan"]
new_city = input("Enter a new city to add: ")
cities.append(new_city)
print("Updated list of cities:", cities)

# 8️⃣ Create list of 5 words and print each in reverse order
words = ["python", "code", "learn", "fun", "logic"]
print("Words in reverse order:")
for word in reversed(words):
    print(word)

# 9️⃣ Take three marks, calculate total, average, and grade
mark1 = float(input("Enter mark 1: "))
mark2 = float(input("Enter mark 2: "))
mark3 = float(input("Enter mark 3: "))
total = mark1 + mark2 + mark3
average = total / 3

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Total:", total)
print("Average:", average)
print("Grade:", grade)

# 🔟 Create list of fruits and check if "apple" is in it
fruits = ["banana", "mango", "apple", "grape"]
if "apple" in fruits:
    print("Found")
else:
    print("Not Found")


