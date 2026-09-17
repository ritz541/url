def my_hash(text):
    total = 0
    for char in text:
        total += ord(char)
    return total % 100


print(100 % 10)
print(105 % 100)
print(232 % 100)
print(13532 % 100)
print(13532 % 10)
print(13532 % 1000)
