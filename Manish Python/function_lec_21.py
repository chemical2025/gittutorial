def cost_of_fencing (length, width, cost_per_meter):
    perimeter = 2 * (length + width)
    total_cost = perimeter * cost_per_meter
    return total_cost

# Example usage
length = 10
width = 5
cost_per_meter = 20
total_cost = cost_of_fencing(length, width, cost_per_meter)
print(f"The total cost of fencing is: {total_cost} currency units")

# args and kwargs example
def example_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
example_function(1, 2, 3, name="Alice", age=30)

#  *args take list and convert it to tuple always
def sum (*args):
    total = 0
    for i in args:
        total += i
    return total
print(sum(1, 2, 3))  # Output: 6

def discount_amount (*args, discount_rate=0.1):
    total = 0
    for i in args:
        total += i
    return total - (total * discount_rate)
print(discount_amount(100, 200, 300))  # Output: 60.0

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=30, city="Pune")  # Output: name: Alice, age: 30, city: Pune

'''Here a real-time example: 
Suppose you are creating a function to register a user, 
but the user can provide different optional 
details (like email, phone, address, etc.).
You can use **kwargs to handle this flexibility'''

def register_user(username, **kwargs):
    print(f"Username: {username}")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
# Example usage:
register_user("john_doe", email="sagar@gmail.com", phone="1234567890", address="Pune")

def register_user(username, **kwargs):
    with open("users.txt", "a") as f:
        f.write(f"Username: {username}\n")
        for key, value in kwargs.items():
            f.write(f"{key.capitalize()}: {value}\n")
        f.write("\n")  # Add a blank line between users

# Example usage:
register_user("john_doe", email="john@example.com", phone="1234567890", address="Pune")
register_user("alice", email="alice@example.com")

'''This function reads a file and returns a list of unique records.
It raises an error if the file is empty.'''

def read_unique_records(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        if not lines:
            raise ValueError("File is empty!")
        unique_lines = set(line.strip() for line in lines if line.strip())
        return list(unique_lines)

# Example usage:
try:
    records = read_unique_records("assigment.txt")
    print(records)
except ValueError as e:
    print(e)

