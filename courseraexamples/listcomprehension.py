#multiples of 7 from 7 to 70

multiples=[x*7 for x in range(1,11)]
print(multiples)

#lenghts of string in a list
languages=["python","c","pearl","Go"]
lengths=[len(language) for language in languages]
print(lengths)

#numbers divisible by 3 between 1 and 100
numbers=[x for x in range(1,101) if x%3==0]
print(numbers)

def skip_elements(elements):
    new=[x for index,x in enumerate(elements) if index%2 ==0]
    return new  

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']