my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("list: ", my_list)

my_list.insert(1, 15)
print("list after inserting values from 1 to 15: ", my_list)
my_list.extend([50, 60, 70])
print("list after inserting values from 50 to 70: ", my_list)
my_list.pop()
print("list after removing last value: ", my_list)
my_list.sort()
print("list after sorting: ", my_list)

index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)