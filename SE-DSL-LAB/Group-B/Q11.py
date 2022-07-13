# Write a Python program to store roll numbers of student in array who attended
# training program in random order. Write function for searching whether particular
# student attended training program or not, using Linear search and Sentinel search.

import random

student_list = [random.randint(-100, 100) for i in range(10)]
print(student_list)


def linear_search(l, key):
    # O(n)
    for i in range(len(l)):
        if l[i] == key:
            return i
    return -1


def sentinel_search(l, key):
    # O(n)
    last_element = l[-1]
    l[-1] = key
    i = 0
    while l[i] != key:
        i += 1  # i = i+1

    if i != len(l) - 1:
        return i
    elif last_element == key:
        return len(l) - 1
    else:
        return -1


key = random.choice(student_list)
print(key)

print(sentinel_search(student_list, student_list[-1]))
