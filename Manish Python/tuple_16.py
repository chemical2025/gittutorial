tup = (1,3,4,'ram',5.6,True)
sun = (33,45,2,'tona','ram',33,'hi')
final = tup + sun
print(final)

# Tuple is immutable, so we cannot change the value of an element
print(tup[0]) 

print(tup[1:4])  # Slicing a tuple
print(tup[1:])   # Slicing from index 1 to the end
print(tup[:4])   # Slicing from the start to index 4
print(tup[-1])   # Accessing the last element
print(tup[-2])   # Accessing the second last element
print(tup[1:4:2])  # Slicing with a step of 2

print(tup.count(3))  # Counting occurrences of an element
print(tup.index('ram'))  # Finding the index of an element

# Converting a tuple to a list
test = ([1, 2, 3], [4, 5, 6],[1],[2,3]) #converting a list of lists to a single tuple
output = (1, 2, 3, 4, 5, 6, 1, 2, 3) # this how it should look like
result = ()
for i in test:
    new = tuple(i)
    result += new
print(result)  # Output: (1, 2, 3, 4, 5, 6, 1, 2, 3)

# output i want is exponesion of tup1 and tup2

tup1 = (10, 2, 3)
tup2 = (3, 5, 6)
print(tup1[1] ** tup2[1])
output = ()
for i in range(len(tup1)):
    output += (tup1[i] ** tup2[i],)
print(output)  # Output: (1000, 32, 729)
