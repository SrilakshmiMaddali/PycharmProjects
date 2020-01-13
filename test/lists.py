'''
#find max number
num_list=[12,14,15,16,68,900]
print(max(num_list))

#delete duplicates
numbers=[1,2,3,3,4,5,5,222,222,222]
num=0
for x in numbers:
    num=x
    for y in range(len(numbers)):
        if numbers.count(num)>1:
            numbers.remove(num)

print(numbers)
'''
#delete duplicates using another list
numbers=[1,1,2,2,3,3,3,4,4]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

