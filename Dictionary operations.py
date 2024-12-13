# Creating a sample dictionary 
sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
 
# Checking if a key exists in the dictionary 
key_to_check = 'b' 
if key_to_check in sample_dict: 
    print(f'The key "{key_to_check}" exists in the dictionary.') 
 
# Traversing the dictionary using a loop 
print("Traversing the dictionary:") 
for key, value in sample_dict.items(): 
    print(f'Key: {key}, Value: {value}') 
 
# Dictionary methods 
keys_list = list(sample_dict.keys()) 
values_list = list(sample_dict.values()) 
items_list = list(sample_dict.items()) 
 
print("\nUsing dictionary methods:") 
print(f'Keys: {keys_list}') 
print(f'Values: {values_list}') 
print(f'Items: {items_list}')
