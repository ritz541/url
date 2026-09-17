CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_base(n):
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        n, rem = divmod(n, 62)
        result = CHARS[rem] + result
    return result

print(to_base(1))
print(to_base(23))
print(to_base(100))
print(to_base(63))
print(to_base(999999))
