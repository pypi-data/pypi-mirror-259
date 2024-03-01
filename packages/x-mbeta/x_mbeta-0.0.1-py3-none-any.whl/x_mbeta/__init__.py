import random


def get_random_password(num):
    list1 = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]
    value = ""
    for i in range(num):
        value = value + list1[random.randint(0, len(list1) - 1)]
    return value
