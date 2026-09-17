def my_hash(text):
    total = 0
    for char in text:
        total += ord(char)
    return total % 5

print(my_hash("ab"))
print(my_hash("ba"))
