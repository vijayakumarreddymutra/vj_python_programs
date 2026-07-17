import random

a = random.sample(range(23, 76), 10)

print(a)

def biggest_num(list1):
    b = float("-inf")

    for i in list1:
        if i > b:
            b = i

    return b
print(biggest_num(a))


def smallest_number(list2):
    b = float("inf")

    for i in list2:
        if i < b:
            b = i

    return b
print(smallest_number(a))