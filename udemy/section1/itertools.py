from itertools import count,accumulate,takewhile


for x in count(3):
    print(x)
    if x==20:
        break

### accumulates the previous numbers and add to the current number for eg in a range of 4
#0,1+0,2+1+0,3+2+1+0,4+3+2+1+0
numbers=list(accumulate(range(5)))
print(numbers)
print(list(takewhile(lambda x: x<=6,numbers)))
