# 1️⃣ Print every 3rd number from 3 to 30
print("1️⃣ Every 3rd number from 3 to 30:")
for i in range(3, 31, 3):
    print(i)

# 2️⃣ Sum of even numbers from 2 to 20
print("\n2️⃣ Sum of even numbers from 2 to 20:")
even_sum = sum(i for i in range(2, 21, 2))
print(even_sum)

# 3️⃣ Product of odd numbers from 1 to 9
print("\n3️⃣ Product of odd numbers from 1 to 9:")
product = 1
for i in range(1, 10, 2):
    product *= i
print(product)

# 4️⃣ List of 5 names and print each on a new line
print("\n4️⃣ Names:")
names = ["Ali", "Sara", "John", "Ayesha", "Hamza"]
for name in names:
    print(name)

# 5️⃣ Count how many letters 'a' in "banana"
print("\n5️⃣ Count of 'a' in 'banana':")
print("banana".count('a'))

# 6️⃣ Print only negative numbers from a list
print("\n6️⃣ Negative numbers from list:")
nums = [4, -1, -7, 5, 0, -3]
for num in nums:
    if num < 0:
        print(num)

# 7️⃣ Numbers ending in 5 from 1 to 50
print("\n7️⃣ Numbers ending in 5 from 1 to 50:")
for i in range(1, 51):
    if str(i).endswith("5"):
        print(i)

# 8️⃣ Length of each word in ["cat", "elephant", "bat"]
print("\n8️⃣ Length of words:")
words = ["cat", "elephant", "bat"]
for word in words:
    print(f"{word}: {len(word)}")

# 9️⃣ Take 3 numbers from user and print average
print("\n9️⃣ Average of 3 user input numbers:")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
print("Average:", (a + b + c) / 3)

# 🔟 Table of 5 in reverse
print("\n🔟 Table of 5 in reverse:")
for i in range(10, 0, -1):
    print(f"5 x {i} = {5*i}")

# 1️⃣1️⃣ Print all characters in "Python Is Fun"
print("\n1️⃣1️⃣ Characters in 'Python Is Fun':")
for ch in "Python Is Fun":
    print(ch)

# 1️⃣2️⃣ Print every second item from a list of numbers
print("\n1️⃣2️⃣ Every second item:")
numbers = [10, 20, 30, 40, 50, 60]
for i in range(1, len(numbers), 2):
    print(numbers[i])

# 1️⃣3️⃣ Count consonants in a word
print("\n1️⃣3️⃣ Count consonants in a word:")
word = input("Enter a word: ").lower()
consonants = [ch for ch in word if ch.isalpha() and ch not in 'aeiou']
print("Consonants count:", len(consonants))

# 1️⃣4️⃣ Print cubes from 1 to 5
print("\n1️⃣4️⃣ Cubes from 1 to 5:")
for i in range(1, 6):
    print(f"{i}^3 = {i**3}")

# 1️⃣5️⃣ Print words that start with 'a'
print("\n1️⃣5️⃣ Words starting with 'a':")
word_list = ["apple", "banana", "air", "kite", "angle"]
for word in word_list:
    if word.startswith('a'):
        print(word)

# 1️⃣6️⃣ Numbers from 100 to 110 excluding 105
print("\n1️⃣6️⃣ Numbers from 100 to 110 (excluding 105):")
for i in range(100, 111):
    if i != 105:
        print(i)

# 1️⃣7️⃣ First 5 positive multiples of 4
print("\n1️⃣7️⃣ First 5 multiples of 4:")
for i in range(1, 6):
    print(i * 4)

# 1️⃣8️⃣ Each word in "Coding is easy" on a new line
print("\n1️⃣8️⃣ Words in sentence:")
for word in "Coding is easy".split():
    print(word)

# 1️⃣9️⃣ Print only even numbers from a number list
print("\n1️⃣9️⃣ Even numbers from list:")
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in num_list:
    if num % 2 == 0:
        print(num)
