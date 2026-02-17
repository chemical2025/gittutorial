# i want to use logger.info instead of print so i can get line no of the code
# i will use logging module for this

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


#.1 You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0).
arr = [1,2,3,4,5,6,7,8,9,10]

x = arr[::2]  # Output: [1, 3, 5, 7, 9]
print(x)

output = []

for i in range(len(arr)):
    if i%2==0:
        output.append(arr[i])
    else:
        continue
print(output)  # Output: [1, 3, 5, 7, 9]

#.2 Given an array arr[] of positive integers. The task is to return the count of the number of odd and even elements in the array.

odd = 0
even = 0
for i in arr:
    if i%2 ==0:
        even+=1
    else:
        odd+=1
print(odd, even)

## Day_2.py
# we can itrate strings like lists but we cannot change them or replace them
# strings are immutable

# There are two zeroes in 1004 on replacing all zeroes with 5, the new number will be 1554.
# 1st approach
n = 1004
n = str(n)  # Convert to string
n = n.replace('0', '5')  # Replace '0' with '5
n = int(n)  # Convert back to integer
print(n)  # Output: 1554

# 2nd approach
n = 1004
num = str(n)  # Convert to string
str = ''
for i in num:
    if i == '0':
        str += '5'  # Replace '0' with '5'
    else:
        str += i  # Keep other digits unchanged
print(int(str))  # Output: 1554

# Given a string s, the task is to change the complete string to uppercase or lowercase depending on the case of the first character.

x="AbCD"
y= ""
for i in (x):
    if x[0].isupper():
        y = x.upper()
    elif x[0].islower():
        y = x.lower()
print(y)  # Output: abcd (if x starts with lowercase) or ABCD (if x starts with uppercase)


# Day_3.py
# Given an integer n, your task is to compute the sum of all natural numbers from 1 to n (inclusive). If n is 0, the sum should be 0.
# Example: If n = 5, the sum should be 1 + 2 + 3 + 4 + 5 = 15.
n = 5
o = 0
for i in range(n + 1):
    if n == 0:
        o = 0
    else:
        o += i  # Calculate the sum of numbers from 1 to n
print(o)  # Output: 15 (sum of numbers from 1 to 5)

# You are given an integer array arr[]. The task is to find the sum of it.
arr = [1, 2, 3, 4]
sum_arr = 0
for i in arr:
    sum_arr += i  # Calculate the sum of elements in the array
print(sum_arr)  # Output: 10 (sum of elements in the array)

# Day_4.py

# Given a string. Count the number of Camel Case characters in it.
s = "CamelCaseString"
camel_case_count = 0
for char in s:
    if char.isupper():  # Check if the character is uppercase
        camel_case_count += 1  # Increment the count for each uppercase character
print(camel_case_count)  # Output: 3 (C, S, and C are uppercase characters)

# Given a string S, write a program to count the occurrence of Lowercase characters, Uppercase characters, Special characters and Numeric values in the string. 
# Note: There are no white spaces in the string.

s = "HelloWorld123!@#"
lowercase_count = 0
uppercase_count = 0
special_count = 0
numeric_count = 0
for char in s:
    if char.islower():  # Check if the character is lowercase
        lowercase_count += 1
    elif char.isupper():  # Check if the character is uppercase
        uppercase_count += 1
    elif char.isdigit():  # Check if the character is numeric
        numeric_count += 1
    else:  # If it's neither, it must be a special character
        special_count += 1

# Day_5.py
#Given an array arr[]. The task is to find the largest element and return it.
arr = [22, 45, 9, 3, 67, 1, 89, 34]
x = sorted(arr)  # Sort the array in descending order
range = len(x) - 1  # Get the index of the largest element
print(f"range {range}")  # Output the sorted array
if range >= 0:  # Check if the array is not empty
    largest_element = x[range]  # The last element in the sorted array is the largest
    print(largest_element)  # Output: 9 (the largest element in the array)

# alternative approach
mx = float('-inf')  # Initialize mx to negative infinity
for i in arr:
    if i > mx:  # Check if the current element is greater than mx
        mx = i  # Update mx to the current element if it's larger
print(mx)  # Output: 89 (the maximun element in the array)

# Given an integer k and array arr. Your task is to return the position of the first occurrence of k in the given array and if element k is not present in the array then return -1.
# Note: 1-based indexing is followed here.
k = 16
arr = [12, 34, 16, 45, 67]
position = -1  # Initialize position to -1 (not found)

# for i in range(len(arr)):
#     if arr[i] == k:  # Check if the current element matches k
#         position = i + 1  # Update position (1-based index)
#         break  # Exit the loop after finding the first occurrence
# print(position)  # Output: 3 (the first occurrence of 16 is at index 2 in 0-based, so 3 in 1-based indexing)

# Day_6.py
# Given a string s of lowercase alphabets, You have to check that  it is isogram or not.
# An Isogram is a string in which no letter occurs more than once.
s = "machinee"
is_isogram = True  # Assume it is an isogram initially
for char in s:
    if s.count(char) > 1:  # Check if the character appears more than once
        is_isogram = False  # If it does, it's not an isogram
        break  # Exit the loop early if a duplicate is found
print(is_isogram)  # Output: True (since "machine" has no repeating letters)

#alternative approach
s = "machine"
res = {}
for i in s:
    if i in res:
        print (False)  # If the character is already in the dictionary, it's not an isogram
    else:
        res[i] = 1
print(True)  # If no duplicates were found, it's an isogram

# Day_7.py
# Given a number n, determine whether it is a prime number or not.
#Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
# n= 29
# start = 2
# end = n//2
# for i in range(start,end):
#     if n%i == 0:
#         print (False)
# print(True)

# Given an array arr[], swap the kth element from the beginning with the kth element from the end.
#Note: 1-based indexing is followed.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
if k <= len(arr) // 2:  # Check if k is within the valid range
    arr[k - 1], arr[-k] = arr[-k], arr[k - 1]  # Swap the kth element from the start with the kth from the end
logger.info(arr)  # Output: [1, 2, 7, 4, 5, 6, 3, 8, 9] (3rd element swapped with 3rd from the end)

# Day_8.py
s = "HelloWorld"
# Given a string s, your task is to reverse the string.
reversed_s = s[::-1]  # Reverse the string using slicing
logger.info(reversed_s)  # Output: "dlroWolleH"

# other approach
# reversed_s = ''
# for char in range(len(s) - 1, -1, -1):  
#     reversed_s = reversed_s + s[char]  # Append characters in reverse order
# logger.info(reversed_s)  # Output: "dlroWolleH"

# Day_9.py
# Given a string s, your task is to check whether the string is a palindrome or not.
s = "madam"
is_palindrome = s == s[::-1]  # Check if the string is equal to its reverse
logger.info(is_palindrome)  # Output: True (since "madam" reads the same forwards and backwards)
# other approach
# is_palindrome = True
# for i in range(len(s) // 2):
#     if s[i] != s[-(i + 1)]:  # Compare characters from both ends
#         is_palindrome = False  # If any characters don't match, it's not a palindrome
# logger.info(is_palindrome)  # Output: True (since "madam" is a palindrome)

# arr = [1,2,3,2,1]
# rev = []
# for i in range(len(arr) - 1, -1, -1):  # Iterate from the end to the start
#     rev.append(arr[i])  # Append elements in reverse order
# if arr == rev:  # Check if the original array is equal to the reversed array
#     logger.info(True)  # Output: True (since [1, 2, 3, 2, 1] is a palindrome)
# else:
#     logger.info(False)

# Given an array, arr[] of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.
arr = [1, 2, 3, 4, 5]
x = 3
index = -1  # Initialize index to -1 (not found)
# for i in range(len(arr)):
#     if arr[i] == x:  # Check if the current element matches x
#         index = i  # Update index to the current position
#         break  # Exit the loop after finding the first occurrence

# Day_10.py
# Given a string consisting of lowercase english alphabets. Find the repeated character present first in the string.

# NOTE - If there are no repeating characters return '#'.
s = "bcdfgabb"
repeated_char = '#'
seen = set()  # Create a set to track seen characters
for char in s:
    if char in seen:  # Check if the character has been seen before
        repeated_char = char  # Update repeated_char to the first repeating character
        break  # Exit the loop after finding the first repeating character
    seen.add(char)  # Add the character to the set of seen characters
logger.info(repeated_char)  # Output: 'a' (the first repeating character)

# Other approach
out = {}
for i in s:
    if i in out:
        out[i] += 1  # Increment the count for the character
    else:
        out[i] = 1
for k, v in out.items():
    if v > 1:  # Check if the character appears more than once
        logger.info(k)  # Output: 'a' (the first repeating character)
        break
print('#')  # If no repeating character is found, print '#'

# Given a string s consisting of lowercase English Letters. return the first non-repeating character in s. If there is no non-repeating character, return '$'.
s = "abacabad"
out = {}
for i in s:
    if i in out:
        out[i] += 1  # Increment the count for the character
    else:
        out[i] = 1
for k, v in out.items():
    if v == 1:  # Check if the character appears more than once
        logger.info(k)  # Output: 'a' (the first repeating character)
        break
print('$')

# Day_11.py

# You are given an array arr[] where no two adjacent elements are same, find the index of a peak element. An element is considered to be a peak if it is greater than its adjacent elements (if they exist).

#If there are multiple peak elements, Return index of any one of them. The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".

#Note: Consider the element before the first element and the element after the last element to be negative infinity.

arr = [1, 3, 20, 4, 1, 0]
arr.insert(0, float('-inf'))
arr.append(float('-inf'))
start = 1
end = len(arr) - 1
# for i in range(start,end):
#     if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
#         print(i)
#     else:
#         continue
# print (False)

# Given an array arr. Your task is to find the minimum and maximum elements in the array.

#Note: Return a Pair that contains two elements the first one will be a minimum element and the second will be a maximum.

arr = [13, 1, 23, 45, 670, 80, 100]
mx = float('-inf')
mn = float('inf')
for i in arr:
    if i > mx:
        mx = i
    if i < mn:
        mn = i
print(mn, mx)

# how to write and read df in pyspark
# from pyspark.sql import SparkSession
# spark = SparkSession.builder.appName("example").getOrCreate()
# df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)
# df.write.csv("path/to/output.csv", header=True)
# what if for differ file formats like parquet, json, etc.
# df = spark.read.parquet("path/to/file.parquet")
# df.write.parquet("path/to/output.parquet")
# df = spark.read.json("path/to/file.json")
# df.write.json("path/to/output.json")
# df = spark.read.orc("path/to/file.orc")
# df.write.orc("path/to/output.orc")
# df = spark.read.text("path/to/file.txt")
# df.write.text("path/to/output.txt")
# df = spark.read.format("csv").option("header", "true").load("path/to/file.csv")
# df.write.format("csv").option("header", "true").save("path/to/output.csv")
# how spark sql use for reading this df
# df.createOrReplaceTempView("my_table")
# result = spark.sql("SELECT * FROM my_table WHERE column_name = 'value'")
