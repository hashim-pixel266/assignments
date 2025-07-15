# 1️⃣ Create and update set
s = {10, 20, 30}
s.add(50)
s.update([40, 60])
print("Final set:", s)

# 2️⃣ Remove vs discard
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")     # Works fine
fruits.discard("orange")    # Does not throw error
# fruits.remove("orange")   # This would raise KeyError
print("Fruits after remove/discard:", fruits)

# 3️⃣ pop() and clear()
colors = {"red", "green", "blue"}
colors.pop()  # Removes a random item
print("After pop:", colors)
colors.clear()
print("After clear:", colors)

# 4️⃣ Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

# 5️⃣ Subset, Superset, Disjoint
A = {1, 2, 3}
B = {1, 2}
print("B is subset of A:", B.issubset(A))
print("A is superset of B:", A.issuperset(B))
print("A and B are disjoint:", A.isdisjoint(B))

# 6️⃣ Frozenset immutability
vowels = frozenset(['a', 'e', 'i', 'o', 'u'])
try:
    vowels.add('y')
except AttributeError as e:
    print("Error (add):", e)
try:
    vowels.remove('a')
except AttributeError as e:
    print("Error (remove):", e)
# ❗ frozenset is immutable — it cannot be changed after creation

# 7️⃣ Frozenset operations
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([2, 3, 4])
print("Union:", fs1 | fs2)
print("Intersection:", fs1 & fs2)
print("Difference (fs1 - fs2):", fs1 - fs2)
print("Symmetric Difference:", fs1 ^ fs2)

# 8️⃣ Membership and disjoint
cities = {"Lahore", "Karachi", "Islamabad"}
check_list = ["Lahore", "Multan", "Peshawar"]
for city in check_list:
    print(f"{city} is in set:", city in cities)
new_set = {"Peshawar", "Quetta"}
print("Disjoint with new_set:", cities.isdisjoint(new_set))

# 9️⃣ Set operators explained
setA = {1, 2, 3}
setB = {3, 4, 5}
print("Union (|):", setA | setB)  # Combines all unique elements
print("Intersection (&):", setA & setB)  # Common elements
print("Difference (-):", setA - setB)  # Elements in A not in B
print("Symmetric Difference (^):", setA ^ setB)  # Elements not common in both

# 🔟 Input → set → frozenset → test immutability
user_input = input("Enter comma-separated items: ").split(",")
item_set = set(user_input)
item_frozen = frozenset(item_set)
print("Unique items (set):", item_set)
print("Immutable frozenset:", item_frozen)
try:
    item_frozen.add("new_item")
except AttributeError as e:
    print("Error (frozenset add):", e)
# ⚠️ frozensets are immutable — no add/remove possible
