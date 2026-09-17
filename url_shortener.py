import sys
import random
import string

url_store = {}

if len(sys.argv) < 3:
    print("Usage: python3 url_shortener.py <command> [args...]")
elif sys.argv[1] == "shorten":
    url = sys.argv[2]

code = "".join(random.choices(string.ascii_letters + string.digits, k=6))
print(code)
