from string import digits
from string import ascii_lowercase
from string import ascii_uppercase


# "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = digits + ascii_lowercase + ascii_uppercase


# recursive
def ten2any1(n, b):
    assert b <= len(alphabet)

    n, index = divmod(n, b)

    if n > 0:
        return ten2any1(n, b) + alphabet[index]
    else:
        return alphabet[index]


# iterative
def ten2any2(n, b):
    assert b <= len(alphabet)

    ret = ""
    while n > 0:
        n, index = divmod(n, b)
        ret = alphabet[index] + ret

    return ret


if __name__ == '__main__':
    assert ten2any1(5, 2) == '101'
    assert ten2any2(5, 2) == '101'
