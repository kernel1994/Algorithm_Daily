from string import digits
from string import ascii_lowercase
from string import ascii_uppercase


# "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = digits + ascii_lowercase + ascii_uppercase


def any2ten(s, base):
    n = 0

    for i, c in enumerate(reversed(s)):
        index = alphabet.index(c)
        n += index * pow(base, i)

    return n


if __name__ == '__main__':
    assert any2ten('101', 2) == 5
