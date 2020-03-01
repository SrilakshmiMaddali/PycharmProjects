def group_list(group, users):
  members = ",".join(users)
  return group+": "+members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

#with out enumerate function
def skip_elements(elements):
	# code goes here
	newel=[]
	if len(elements)>0:
	  for element in elements:
	    if elements.index(element) %2 ==0:
	      newel.append(element)

	return newel

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []


#using enumerate function
def skip_elements(elements):
	# code goes here
	new=[]
	
	for index,element in enumerate(elements):
	  if index%2==0:
	    new.append(element)
	  
	
	return new

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']



##########################################################


def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  result=[]
  result= list2+list1[::-1] 
  return result
  
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

##############################################

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)


##################################Sorting lists with different parameters 

numbers=[3,2,1,4]
#sorts the original list
numbers.sort()
print(numbers)

names=["Sri","Lakshmi","Pavan","Bhuvan","Kasyap"]
#original list remains the same
print(sorted(names))
#sorting by length of the name using key value
print(sorted(names,key=len))


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
print(list1+list2)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)