CHARS = "0123457890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(n):
    if n == 0:
        return CHARS[n]
    out = []
    while n > 0:
        n, rem = divmod(n, 62)
        out.append(CHARS[rem])
    return "".join(reversed(out))


def from_base(code):
    n = 0
    for char in code:
        n = n * 62 + CHARS.index(char)
    return n
