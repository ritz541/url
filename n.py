store = {}
counter = 1

def expand(code):
    return store.get(code)

def shorten(long_url):
    global counter
    code = str(counter)
    store[code] = long_url
    counter = counter + 1
    return code

code1 = shorten("https://youtube.com")
code2 = shorten("https://google.com")

print("codes:", code1, code2)
print("store: ", store)
print(expand("1"))
print(expand("2"))
print(expand("3"))
