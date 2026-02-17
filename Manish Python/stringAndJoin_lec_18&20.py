# name = 'chetan mavale'
# # we done slicing on string
# print(name[:5])  # Output: ' chet'
# print(name[6:])  # Output: 'mavale'

# # methods on string
# print(name.upper())  # Convert to uppercase
# print(name.lower())  # Convert to lowercase
# print(name.title())  # Convert to title case
# print(name.strip())  # Remove leading and trailing spaces
# print(name.replace('chetan', 'Chetan'))  # Replace substring
# print(name.split())  # Split string into a list of words
# print(name.find('mavale'))  # Find the index of a substring
# print(name.count('a'))  # Count occurrences of a character
# print(name.islower())  # Check if all characters are lowercase
# print(name.isupper())  # Check if all characters are uppercase
# print(name.isalpha())  # Check if all characters are alphabetic
# print(name.isdigit())  # Check if all characters are digits
# print(name.isalnum())  # Check if all characters are alphanumeric
# print(name.startswith(' chetan'))  # Check if string starts with a substring
# print(name.swapcase())  # Swap case of characters

# name = 'chetan mavale'
# name1 = name.split()  # Split the string into a list of words
# lst = []
# for i in name1:
#     if i.startswith('m'):
#         lst.append(i)
# print(lst)  # Output: ['mavale']

email = "sagar12@gamil.com mohann23@gamil.com"
#i want to hide some part of email address by **** like sa***12@gamil.com, mo***23@gamil.com
email = " ".join(email.split())  # Remove extra spaces
# Hiding part of email addresses
emails = email.split()
hidden_emails = []
for i in emails:
    parts = i.split('@')
    hidden_email = parts[0][:2] + '***' + parts[0][3:] + '@' + parts[1]
    hidden_emails.append(hidden_email)
print(hidden_emails)  # Output: ['
# Extracting usernames from email addresses
emails = email.split()
usernames = []
for i in emails:
    usernames.append(i.split('@')[0])
print(usernames)  # Output: ['sagar12', 'mohan23']
# Masking usernames in email addresses
for i in emails:
    parts = i.split('@')
    username = parts[0]
    if len(username) > 2:
        masked = username[0] + '*' * (len(username) - 2) + username[-1]
    else:
        masked = username  # Too short to mask
    masked_email = masked + '@' + parts[1]
    usernames.append(masked_email)
print(usernames)

my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]

# Join ( by using it we can convert list/tupe/set/dictionary to string)
my_list = ['ram', 'shyam', 'sita']
my_string = ' '.join(my_list)
print(type(my_string))  # Output: 'ram shyam sita'

my_dict = {'a': 1, 'b': 2}
my_string = ', '.join(my_dict)
print(my_string)  # Output: 'a, b'

# 

quey = "select * from (SELECT * FROM emp JOIN department ON emp.id = department.id) a WHERE emp.salary > 1000"
sql_dict = [
    {"state": "bihar", "department": "IT"},
    {"state": "maharashtra", "department": "HR"}
]

final_result = []
for i in sql_dict:
    for key, value in i.items():
        final_result.append(f"{key} = '{value}'")
print(final_result)  # Output: ["state = 'bihar'", "department = 'IT'", "state = 'maharashtra'", "department = 'HR'"]

result = " OR ".join(final_result)
print(result)  # Output: "state = 'bihar' OR department = 'IT

print(quey + " AND " + result)  # Output: SQL query with conditions

print("End of code")

for i in emails:
    parts = i.split('@')
    if len(parts) > 1:
        print(f"Username: {parts[0]}, Domain: {parts[1]}")
    else:
        print(f"Invalid email format: {i}")