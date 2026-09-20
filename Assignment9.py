languages = "Python Java C C++ Python Java Python"

# 1. Convert string into a list
language_list = languages.split()

# 2. Display the list
print("Language list:")
print(language_list)

# 3. Count Python
python_count = language_list.count("Python")
print("\nPython appears:", python_count, "times")

# 4. Remove duplicate language names
unique_languages = list(dict.fromkeys(language_list))

print("\nUnique languages:")
print(unique_languages)

# 5. Join unique languages using |
result = " | ".join(unique_languages)

print("\nJoined languages:")
print(result)