# Nested List
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list)

#Length of the List
length=len(list)
print('length of the list',length)

# Concatenation of Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)

Python Membership Operators
The Python membership operators test for the membership of an object in a sequence, such as strings, lists, or tuples.
# Membership Check
print(2 in list1)
print(3 not in list2)

# Iterate over a list
for i in list1:
    print(i)
The index() method returns the position at the first occurrence of the specified value.
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("apple")

print(x)

# Slicing
List = [50, 70, 30, 20, 90, 10, 50]
# Display list
print(List[1:5])
