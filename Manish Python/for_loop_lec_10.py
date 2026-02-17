# lst = [1,11,23,45,67,89,100]
# for i in lst:
#     print(i)
# print("End of loop")

name = ["John", "Alice", "Bob", "Diana"]
name[1:3]
print(name)
for i in range(len(name)):
    print(f" labor {i+1} is {name[i]}")

for i in range(5):
    print( "*" * (i + 1))

for i in range(5):
    print("*" * (5 - i))

for i in range(101):
    if i % 2 != 0:
        print(i, end=" ")

paragraph = """ Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
data warehouse and business intelligence industry’s thought leader on the dimen
sional approach. He has educated tens of thousands of IT professionals. The Toolkit 
books written by Ralph and his colleagues have been the industry’s best sellers 
since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph 
coinvented the Star workstation, the fi rst commercial product with windows, icons, 
and a mouse, at Xerox’s Palo Alto Research Center (PARC). Ralph has a PhD in 
electrical engineering from Stanford University """
count = 0

para=paragraph.lower().split(" ")

for i in para:
    if i == "the":
        count += 1
    else:
        continue
print(f"The word 'the' appears {count} times in the paragraph.")

apple = input("Enter the name of the fruit: ")
banana = input("Enter the name of the fruit: ")
fruit = apple + " " + banana
print(fruit)