def function():
    counter=0
    while counter<5:
        yield counter
        counter += 1


for x in function():
    print(x)


def even_numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


print(list(even_numbers(31)))