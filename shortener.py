from functions import from_base, to_base

db = {}
counter = 1


def shorten(long_url):
    global counter
    code = to_base(counter)
    db[code] = long_url
    counter += 1
    return code


def expand(code):
    return db.get(code)


c1 = shorten("https://www.google.com")
print("short code for google:", c1)
print(f"expand {c1}: {expand(c1)}")


c2 = shorten("https://www.chavanpatil.com")
print(f"short code for chavanpatil: {c2}")
print(f"expand {c2}: {expand(c2)}")
