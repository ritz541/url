buckets = [[], [], [], [], []]

def my_hash(text):
    total = 0
    for char in text:
        total += ord(char)
    return total % 5

code = my_hash("hello")
print("'hello' goes to bucket: ", code)
buckets[code].append("https://google.com")
print("Bucket contents: ", buckets)

code2 = my_hash("fuck")
print("'fuck' goes to bucket", code2)
buckets[code2].append("https://amazon.com")
print("Bucket contents: ", buckets)

code3 = my_hash("slut")
print("'slut' goes to bucket: ", code3)
buckets[code3].append("https://slut.com")
print("Bucket contents: ", buckets)

code4 = my_hash("pussy")
print("'pussy' goes to bucket: ", code4)
buckets[code4].append("https://chavanpatil.com")
print("Bucket contents: ", buckets)


target = "pussy"
bucket_num = my_hash(target)
print("\nLooking for: ", target)
print("It's in bucket:", bucket_num)
print("Bucket contents:", buckets[bucket_num])

for text in buckets[bucket_num]:
    if my_hash(target) == my_hash(text):
        print(text)
    else:
        print('nope')

