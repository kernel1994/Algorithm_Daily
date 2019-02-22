from string import digits
from string import ascii_lowercase
from string import ascii_uppercase


# "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = digits + ascii_lowercase + ascii_uppercase


# recursive
def ten2any1(n, b):
    n, index = divmod(n, b)

    if n > 0:
        return ten2any1(n, b) + alphabet[index]
    else:
        return alphabet[index]


if __name__ == '__main__':
    assert ten2any1(5, 2) == '101'
