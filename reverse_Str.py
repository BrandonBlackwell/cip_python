# Reverse string
str = ["h", "e", "l", "l", "o"]


def reverse(str):
    str[:] = str[::-1]
    return str


print(reverse(str))
