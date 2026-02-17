
# print(len(lst))  # prints 5
# print(lst[0])    # prints 1
# lst.append(6)
# print(lst)       # prints [1, 2, 3, 4,

# st = ['ram', 'shyam', 'hari']
lst = [1, 2, 3, 4, 5]
# lst.insert(-2, 'inserted')

# st.extend(lst)
# print(st)

# line = [['ram', 'shyam'], ['hari', 'gita']]
# print(line[0][1])  
# print(line[1][1])  
print(lst[1:4])
print(lst[::-1])
print(len(lst))

x = 210
if x < 100:
    print("x is less than 100")
elif x > 200:
    print("x is greater than 200")
else:
    print("x is between 100 and 200")

wage=lst.pop(1)
print(wage)  # prints 5, the last element of the list
if wage > 3:
    print("Wage is greater than 3")
elif wage < 1:
    print("Wage is less than 3")
else:
    print("Wage is equal to 3")