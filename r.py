db = {}
counter = 1

def shorten(long_url):
    global counter

    for code, url in db.items():
        if url == long_url:
            return code

    code = str(counter)
    db[code] = long_url
    counter += 1
    return code

def expand(code):
    return db.get(code)

print(shorten("https://chavanpatil.com"))
print(shorten("https://google.com"))
print(shorten("https://chavanpatil.com"))

print(db)

print(expand("1"))
print(expand("2"))
print(expand("3"))
