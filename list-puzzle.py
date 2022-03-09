# Write a Python program that accept a list of integers and check the length and the fifth element.
# Return true if the length of the list is 8 and fifth element occurs thrice in the list


list1 = [10, 21, 45, 78, 45, 78, 78, 40, 45]
print(len(list1))
if  len(list1)>=8 and list1.count(45) == 3:
    print(True)
    print("the length of the list is:", len(list1))
    print("fifth element appeared thrice in a list")