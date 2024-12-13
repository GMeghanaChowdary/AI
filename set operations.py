Software used: Jupyter notebook 
Code: 
set1={1,2,3,4,5} 
set2={3,4,5,6,7} 
#union of set 1 and set2 
union_set=set1.union(set2) 
print(union_set,"union set") 
#intersection of set1 and set2 
intersection_set=set1.intersection(set2) 
print(intersection_set,"intersection set") 
#Difference of set1 and set2 
difference_set1=set1.difference(set2) 
print(difference_set1,"set1-set2") 
#symmetric difference 
symmetric_difference_set=set1.symmetric_difference(set2) 
print(symmetric_difference_set,"symmetric difference set") 
#check if sets have common elements 
have_common_elements=set1.isdisjoint(set2) 
print("Do set1 and set2 have any common elements?",not have_common_elements) 
#Adding an element to a set 
set1.add(6) 
print("set1 after adding element:",set1) 
#Removing an element from a set 
set1.remove(3) 
print("set1 after removing element:",set1)
