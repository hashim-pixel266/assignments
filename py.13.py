# 1️⃣ Create data.txt and write 3 lines
file = open("data.txt", "w")
file.write("This is line one.\n")
file.write("This is line two.\n")
file.write("This is line three.\n")
file.close()

# 2️⃣ Read all lines from data.txt and print one by one
file = open("data.txt", "r")
print("\nReading lines one by one:")
for line in file:
    print(line.strip())
file.close()

# 3️⃣ Use readlines() to print lines with line numbers
file = open("data.txt", "r")
lines = file.readlines()
print("\nUsing readlines() with line numbers:")
for i, line in enumerate(lines, start=1):
    print(f"Line {i}: {line.strip()}")
file.close()

# 4️⃣ Append a new line and print updated content
file = open("data.txt", "a")
file.write("This is the fourth appended line.\n")
file.close()

file = open("data.txt", "r")
print("\nUpdated content of data.txt:")
print(file.read())
file.close()

# 5️⃣ Use with open() and loop to print with line numbers
print("\nUsing with open() and loop:")
with open("data.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"Line {i}: {line.strip()}")

# 6️⃣ Create numbers.txt with 1 to 10, then print the sum
with open("numbers.txt", "w") as file:
    for num in range(1, 11):
        file.write(f"{num}\n")

total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())
print(f"\nSum of numbers from 1 to 10 is: {total}")

# 7️⃣ Create even_numbers.txt with even numbers from 1 to 50
with open("even_numbers.txt", "w") as file:
    for num in range(1, 51):
        if num % 2 == 0:
            file.write(f"{num}\n")

# 8️⃣ Create students.txt and print names with character count
with open("students.txt", "w") as file:
    file.write("Ali\nFatima\nHassan\nAreeba\nZain\n")

print("\nStudent names with character count:")
with open("students.txt", "r") as file:
    for name in file:
        name = name.strip()
        print(f"{name} ({len(name)} characters)")

# 9️⃣ Check if "Python" exists in info.txt
with open("info.txt", "r") as file:
    content = file.read()
    if "Python" in content:
        print("\nPython found")
    else:
        print("\nNot found")

# 🔟 Convert file content to uppercase and save to output.txt
with open("data.txt", "r") as file:
    content = file.read().upper()

with open("output.txt", "w") as file:
    file.write(content)

print("\nAll tasks completed successfully.")
