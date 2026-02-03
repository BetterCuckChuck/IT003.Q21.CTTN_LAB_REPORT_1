import random


def generate_random_numbers(count, type):
    numbers = []
    if (type == "int"):
        for _ in range(count):
            numbers.append(random.randint(0, 1000000000))
    elif (type == "float"):
        for _ in range(count):
            numbers.append(random.uniform(0, 1000000000))
    return numbers

lim_count = 1000000

with open('dataset.txt', 'w') as f:
    # Generate increasing
    curlist = []
    curlist = generate_random_numbers(lim_count, "int")
    curlist.sort()
    for num in curlist:
        f.write(f"{num} ")
    f.write("\n")
    curlist = generate_random_numbers(lim_count, "int")
    curlist.sort(reverse=True)
    for num in curlist:
        f.write(f"{num} ")
    f.write("\n")
    for i in range(3):
        curlist = generate_random_numbers(lim_count, "int")
        for num in curlist:
            f.write(f"{num} ")
        f.write("\n")
    for j in range(5):
        curlist = generate_random_numbers(lim_count, "float")
        for num in curlist:
            f.write(f"{num} ")
        f.write("\n")