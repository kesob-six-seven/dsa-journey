"""
=========================================================
🐍 PYTHON FOR DSA: REVISION CHEATSHEET
=========================================================
"""

# ==========================================
# 1. VARIABLES, TYPES & OPERATORS
# ==========================================
# Swapping (No temp variable needed in Python)
a, b = "hello", "world"
a, b = b, a

# Division & Math
x, y = 7, 2
print(x // y)  # Floor division (3)
print(x % y)   # Modulo/Remainder (1)
print(x ** y)  # Exponent/Power (49)

# Booleans & Logical Operators (Truthiness)
# Falsy values: False, None, 0, 0.0, "", [], {}, set()
is_valid = True and (not False) or True

# ==========================================
# 2. STRINGS (Immutable)
# ==========================================
s = "hello world"
# Slicing: [start:stop:step]
print(s[0:5])    # "hello"
print(s[::-1])   # Reverse string: "dlrow olleh"
print(s[-3:])    # Last 3 characters: "rld"

# String Formatting
name, age = "Kesob", 25
print(f"My name is {name} and I am {age}.")

# ==========================================
# 3. LISTS (Arrays - Mutable)
# ==========================================
nums = [1, 2, 3]
nums.append(4)       # Adds to end: O(1)
nums.pop()           # Removes from end: O(1)
nums.pop(0)          # Removes at index 0: O(N) 
nums.insert(0, 1)    # Inserts at index 0: O(N)

# Built-in Math
print(sum(nums), min(nums), max(nums))

# ==========================================
# 4. SETS (Hash Sets - Unordered, Unique)
# ==========================================
# Lookups, insertions, deletions are O(1) average time
my_set = set([1, 2, 2, 3]) # Converts list to set: {1, 2, 3}
my_set.add(4)
my_set.remove(2)
print(4 in my_set)         # O(1) lookup

# ==========================================
# 5. DICTIONARIES (Hash Maps - Key/Value pairs)
# ==========================================
# Lookups, insertions, deletions are O(1) average time
count_map = {"a": 1, "b": 2}

# Safe insertion/incrementing (Building frequency maps)
char = "c"
count_map[char] = count_map.get(char, 0) + 1

# Looping through a Dictionary
for key, value in count_map.items():
    print(key, value)

# Deleting keys safely
if "a" in count_map:
    del count_map["a"]
# OR
count_map.pop("b", None) # Returns None if key doesn't exist, avoids errors

# ==========================================
# 6. LOOPS & CONTROL FLOW
# ==========================================
# Standard For Loop
for i in range(5):          # 0 to 4
    pass

# Range with Step: range(start, stop, step)
for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    pass

# Reverse Loop
for i in range(10, 0, -1):  # 10 down to 1
    pass

# Enumerate (Get index AND value simultaneously)
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)

# ==========================================
# 7. FUNCTIONS & TYPE HINTS
# ==========================================
# Type hints don't enforce types at runtime, but are great for readability
def get_longer_word(word1: str, word2: str) -> str:
    if len(word1) >= len(word2):
        return word1
    return word2

# ==========================================
# 8. INPUT/OUTPUT & ERROR HANDLING
# ==========================================
# Parsing comma-separated input strings into a list
num_string = "1,2,3"
num_list = num_string.split(",") # ['1', '2', '3']

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")