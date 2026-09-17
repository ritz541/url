def my_hash(text):
    total = 0
    for char in text:
        total += ord(char)
    return total % 1000


url_map = {}

def shorten(url):

    code = my_hash(url)

    url_map[code] = url

    return code


def lookup(code):
    return url_map.get(code, "Not found!")


my_url = "https://www.chavanpatil.com"
short_code = shorten(my_url)

print("Original:", my_url)
print("Hash Code:", short_code)
print("Lookup result:", lookup(short_code))

