num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,12,14,16,18,20]
new_list = [2,4,6]

# list comprehension with for loop
new = []
for i in num_list:
    if i % 2 == 0:
        new.append("even")
    else:
        new.append("odd")
print(new)

# list comprehension with if-else
new = ["even" if i % 2 == 0 else "odd" for i in num_list]
print(new)

# list comprehension with if condition
new = [i for i in num_list if i % 2 == 0]
print(new)

lst1= [1, 2, 3, 4, 5]
lst2 = [6, 2, 8, 1, 10]
lst3 = [11, 2, 13, 1, 15]
lst4 = [] # to store common elements
# find common elements in lst1, lst2, and lst3
for i in lst1:
    if i in lst2 and i in lst3:
        lst4.append(i)
print(lst4)